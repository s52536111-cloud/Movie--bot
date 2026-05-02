import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔐 ENV VARIABLES
API_ID = int(os.getenv("38289691"))
API_HASH = os.getenv("475de3b22b9066c0b1e4fd023a8a5da1")
BOT_TOKEN = os.getenv("8658439095:AAGTbzG0sU98KTRUYOk0P4zUoH03Rk_rUO4")
CHANNEL = os.getenv("@utopiaez")  # example: @yourchannel
OMDB_API = os.getenv("de23856a")

app = Client("movie_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 🔐 Force Join Check
async def is_joined(client, user_id):
    try:
        member = await client.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# 🚫 Not Joined Message
def join_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL.replace('@','')}")]
    ])

# 👋 Start Command
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    if not await is_joined(client, user_id):
        return await message.reply(
            "🔒 ആദ്യം നമ്മുടെ ചാനലിൽ join ചെയ്യണം!",
            reply_markup=join_button()
        )

    await message.reply("👋 സ്വാഗതം! Use /movie <name>")

# 🎬 Movie Search
@app.on_message(filters.command("movie"))
async def movie(client, message):
    user_id = message.from_user.id

    if not await is_joined(client, user_id):
        return await message.reply(
            "🔒 ആദ്യം join ചെയ്യണം!",
            reply_markup=join_button()
        )

    if len(message.command) < 2:
        return await message.reply("❗ Usage: /movie KGF")

    query = " ".join(message.command[1:])
    url = f"http://www.omdbapi.com/?apikey={OMDB_API}&t={query}"

    res = requests.get(url).json()

    if res.get("Response") == "False":
        return await message.reply("❌ Movie not found")

    text = f"""🎬 {res.get('Title')}
📅 Year: {res.get('Year')}
⭐ IMDb: {res.get('imdbRating')}
🎭 Genre: {res.get('Genre')}

📝 {res.get('Plot')}
"""

    poster = res.get("Poster")

    if poster and poster != "N/A":
        await message.reply_photo(photo=poster, caption=text)
    else:
        await message.reply(text)

# ▶️ Run
app.run()
