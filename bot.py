from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 1. DEFINE YOUR VARIABLES FIRST
API_ID = int("28289691")
API_HASH = "475de3b22b9066c0b1e4fd023a8a5da1"
BOT_TOKEN = "8658439095:AAGTbzG0sU98KTRUYOk0P4zUoH03Rk_rUO4"
CHANNEL_ID = int(-1003995784518)
FORCE_CHANNEL = "utopiaez"

# 2. NOW CREATE THE CLIENT
bot = Client(
    "movie-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    try:
        await client.get_chat_member(FORCE_CHANNEL, user_id)
    except Exception:
        return await message.reply(
            "🚫 ആദ്യം ചാനൽ ജോയിൻ ചെയ്യണം!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_CHANNEL}")]]
            )
        )

    if len(message.command) > 1:
        file_id = message.command[1]
        try:
            await client.copy_message(message.chat.id, CHANNEL_ID, int(file_id))
        except Exception as e:
            await message.reply(f"Error: {e}")
    else:
        await message.reply("Send movie ID 🎬")

bot.run()
