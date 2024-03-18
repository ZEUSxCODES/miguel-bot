import os
import logging
from pyrogram import Client, filters, idle
from sample_config import Config

bot = Client(
   "NoPMsBot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
    user_id = message.from_user.id
    if user_id == Config.OWNER_ID:
        return await message.reply_text("**Hello Sir!**")
    else:
        mention = message.from_user.mention()
        start_message = (
            f"Hi {mention}\n\n"
            "How are you today?\n"
            "I can deliver your messages to my boss.\n"
            "Just leave your messages & wait for reply.\n"
            "Don't try to spam, else you'll be blocked instantly.\n"
            "I've notified my boss that you've started me!\n\n"
            "Now tell me why you came here?\n"
            "Tap on Help from the menu button or click /help to know more.\n\n"
            "Powered by @anmol0700"
        )
        return await message.reply_text(start_message)

@bot.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    help_text = (
        "Just say 💬\n"
        "Why are you here❓\n\n"
        "➥ Inquiries 🔦\n"
        "➥ Doubts 🤔\n"
        "➥ Problems 😰\n"
        "➥ Help 😟\n"
        "➥ Feedbacks 🔰\n"
        "➥ Promotion 🛒\n"
        "[Your Channel/Group]\n"
        "➥ Donate 💳 [Us]\n\n"
        "🛠 Help Commands 🛠\n"
        "➥ /help\n"
        "➥ /donate\n"
        "➥ /settings\n\n"
        "Powered by @Anmol0700\n\n"
        "✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧"
    )
    await message.reply_text(help_text)

@bot.on_message(filters.text | 
                filters.media | 
                filters.sticker | 
                filters.animation | 
                filters.private | 
                ~filters.command("start") &
                ~filters.command("help"))
async def send_func(_, message):
    user_id = message.from_user.id
    if user_id == Config.OWNER_ID:
        if message.reply_to_message and message.reply_to_message.forward_from:
            forward_user_id = message.reply_to_message.forward_from.id
            try:
                await bot.send_message(chat_id=forward_user_id, text=message.text)
            except Exception as e:
                return await message.reply(str(e))
    else:
        try:
            await message.forward(chat_id=Config.OWNER_ID)
        except Exception as e:
            return await message.reply(str(e))

bot.start()
idle()
