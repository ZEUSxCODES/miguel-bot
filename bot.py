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

settings = {}

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
        "➥ /donate\n"
        "➥ /settings\n\n"
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
        "Donate us to keep our services continuously alive 😢\n"
        "You can send any amount\n"
        "of 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ ...as you wish 😊\n\n"
        "📨 Payment methods 💳\n"
        "GooglePay / Paytm / PhonePay / Net Banking ...\n\n"
        "For donation message me💬 \n"
        "@anmol0700 [or here via this bot]\n\n"
        "Or you can scan the QR code below 👇\n"
        "UPI link 🔗 also there 😇\n\n"
        "Thanking you 🌹\n\n"
        "🛍 UPI ID:\n`anmol0700@fam`"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('💳 Donate 💳', url='https://te.legra.ph/Donate-Us-03-15')],
        [InlineKeyboardButton('👨‍💻 Support Group', url='https://t.me/Movies_Samrajya'),
         InlineKeyboardButton('🔄 Update Channel', url='https://t.me/Film_Nest')]
    ])

    await message.reply_text(donate_message, reply_markup=keyboard)

@bot.on_message(filters.command("settings") & filters.private)
async def settings_command(_, message):
    user_id = message.from_user.id
    if user_id == Config.OWNER_ID:
        return await message.reply_text("You are the owner. You don't need settings.")
    
    mention = message.from_user.mention()
    settings_message = (
        f"{mention}, here you can set your settings:\n\n"
        "✔️ Successfully set notifications to True"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('True', callback_data='set_notification_true'),
         InlineKeyboardButton('False', callback_data='set_notification_false')]
    ])

    settings[message.from_user.id] = True  # Default value for notifications

    await message.reply_text(settings_message, reply_markup=keyboard)

@bot.on_callback_query()
async def callback_handler(_, query):
    user_id = query.from_user.id
    if user_id not in settings:
        return await query.answer("You need to set your settings first!")

    if query.data == 'set_notification_true':
        settings[user_id] = True
        await query.answer("Notifications set to True")
    elif query.data == 'set_notification_false':
        settings[user_id] = False
        await query.answer("Notifications set to False")

bot.start()
idle()
