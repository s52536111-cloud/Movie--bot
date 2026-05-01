from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = int(-100XXXXXXXXXX)
FORCE_CHANNEL = "yourchannelusername"

bot = Client("movie-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    try:
        await client.get_chat_member(FORCE_CHANNEL, user_id)
    except:
        return await message.reply(
            "🚫 ആദ്യം ചാനൽ ജോയിൻ ചെയ്യണം!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_CHANNEL}")]]
            )
        )

    if len(message.command) > 1:
        file_id = message.command[1]
        await client.copy_message(message.chat.id, CHANNEL_ID, int(file_id))
    else:
        await message.reply("Send movie ID 🎬")

bot.run()
