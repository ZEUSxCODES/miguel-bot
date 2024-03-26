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
        mention = message.from_user.mention
        start_message = (
            f"Hi {mention}\n\n"
            "Please mention the purpose, for which you are contacting in a single message (if possible).\n\n"
            "Replies might be delayed\n\n"
            "Merely, spamming start messages would lead to ignoring your valuable messages!\n\n\"
            "🕸This Bot Is Fully Powered By ᴍɪɢᴜᴇʟ ᴏ’ʜᴀʀᴀ!"
        )

        photo_url = "https://te.legra.ph/file/b4faeaa2b1187d9d02f95.jpg"

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('👨‍💻 Bots', url='https://t.me/Film_Nest/25'),
                InlineKeyboardButton('🔄 Channel', url='https://t.me/Film_Nest')
            ]
        ])

        # Sending the photo with caption and the start message
        await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=start_message, reply_markup=keyboard)

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
        "🛍 UPI ID:\n<code>anmol0700@fam</code>"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('💳 Donate 💳', url='https://te.legra.ph/Donate-Us-03-15')]])

    await message.reply_text(donate_message, reply_markup=keyboard)

@bot.on_message(filters.text | 
                filters.media | 
                filters.sticker | 
                filters.animation | 
                filters.private | 
                ~filters.command("start") &
                ~filters.command("help") &
                ~filters.command("donate"))
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
