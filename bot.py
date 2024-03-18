import os
import logging
from pyrogram import Client, filters, idle
from sample_config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
            "Just leave your messages & wait for a reply.\n"
            "Don't try to spam, else you'll be blocked instantly.\n"
            "I've notified my boss that you've started me!\n\n"
            "Now tell me why you came here?\n"
            "Tap on Help from the menu button or click /help to know more.\n\n"
            "Powered by @anmol0700"
        )

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('👨‍💻 Support Group', url='https://t.me/Movies_Samrajya'),
                InlineKeyboardButton('🔄 Update Channel', url='https://t.me/Film_Nest')
            ]
        ])

        return await message.reply_text(start_message, reply_markup=keyboard)

@bot.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    help_text = (
        "Just say 💬\n"
        "Why are you here❓\n\n"
        "➥ Inquiries 🔦\n"
        "➥ Doubts 🤔\n"
        "➦ Problems 😰\n"
        "➥ Help 😟\n"
        "➥ Feedbacks 🔰\n"
        "➥ Promotion 🛒\n"
        "[Your Channel/Group]\n"
        "➥ Donate 💳 [Us]\n\n"
        "🛠 Help Commands 🛠\n"
        "➥ /help\n"
        "➥ /donate\n\n"
        "Powered by @Anmol0700\n\n"
        "✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('👨‍💻 Support Group', url='https://t.me/Movies_Samrajya'),
            InlineKeyboardButton('🔄 Update Channel', url='https://t.me/Film_Nest')
        ]
    ])

    await message.reply_text(help_text, reply_markup=keyboard)

@bot.on_message(filters.command("donate") & filters.private)
async def donate_command(_, message):
    donate_message = (
        "❤️ Thanks for showing interest in donation 😟\n\n"
        "Donate to keep our services continuously alive 😢\n"
        "You can send any amount\n"
        "of 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ ...as you wish 😊\n\n"
        "📨 Payment methods 💳\n"
        "GooglePay / Paytm / PhonePay / Net Banking ...\n\n"
        "For donation, message me💬 \n"
        "@anmol0700 [or here via this bot]\n\n"
        "Or you can scan the QR code below 👇\n"
        "UPI link 🔗 also there 😇\n\n"
        "Thanking you 🌹\n\n"
        "🛍 UPI ID:\n`anmol0700@fam`"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('💳 Donate 💳', url='https://te.legra.ph/Donate-Us-03-15')]])

    await message.reply_text(donate_message, reply_markup=keyboard, parse_mode='markdown')

@bot.on_message(filters.command("broadcast") & filters.private & filters.user(Config.OWNER_ID))
async def broadcast_command(_, message):
    if message.reply_to_message:
        sent_message = message.reply_to_message
        sent_message_text = sent_message.text or sent_message.caption or ""
        
        async for user in bot.iter_users():
            try:
                await bot.send_message(user.id, sent_message_text)
            except Exception as e:
                logging.error(f"Error broadcasting message to {user.id}: {e}")
        await message.reply_text("Broadcast sent successfully!")
    else:
        await message.reply_text("Please reply to a message to broadcast.")

@bot.on_message(filters.text | 
                filters.media | 
                filters.sticker | 
                filters.animation | 
                filters.private | 
                ~filters.command("start") &
                ~filters.command("help") &
                ~filters.command("donate") &
                ~filters.command("broadcast"))
async def send_func(_, message):
    try:
        await message.forward(chat_id=Config.OWNER_ID)
    except Exception as e:
        logging.error(f"Error forwarding message to owner: {e}")

bot.start()
idle()
