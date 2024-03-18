# Copyright (C) 2021 by @ImJanindu
# This programme is a part of Infinity Bots
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging
from pyrogram import Client, filters, idle
from sample_config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

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
        mention = message.from_user.mention(style="md")
        start_message = (
            f"Hi {mention}\n\n"
            "✧✧🌹 ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ? ✧✧\n"
            "➥ ɪ ᴄᴀɴ ᴅᴇʟᴇᴠᴇʀ ʏᴏᴜʀ ᴍᴀssᴀɢᴇs ᴛᴏ ᴍʏ ʙᴏss ✔️\n"
            "➥ᴊᴜsᴛ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ᴍᴀssᴀɢᴇs & ᴡᴀɪᴛ ꜰᴏʀ ʀᴇᴘʟʏ ✉️\n"
            "➥ᴅᴏɴ'ᴛ ᴛʀʏ ᴛᴏ sᴘᴀᴍ, ᴇʟsᴇ ʏᴏᴜ'ʟʟ ʙᴇ ʙʟᴏᴄᴋᴇᴅ ɪɴsᴛᴀɴᴛʟʏ ☠️\n"
            "➥ɪ'ᴠᴇ ɴᴏᴛɪꜰɪᴇᴅ ᴍʏ ʙᴏss ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ sᴛᴀʀᴛᴇᴅ ᴍᴇ! ✆\n\n"
            "💬 ɴᴏᴡ ᴛᴇʟʟ ᴍᴇ ᴡʜʏ ʏᴏᴜ ᴄᴀᴍᴇ ʜᴇʀᴇ❓\n"
            "➥ᴛᴀᴘ ᴏɴ ʜᴇʟᴘ ꜰʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴜᴛᴛᴏɴ ᴏʀ ᴄʟɪᴄᴋ /Help ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ✔️\n\n"
            "🔱 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❗️ @anmol0700"
        )
        return await message.reply_text(start_message)

@bot.on_message(filters.text | 
                filters.media | 
                filters.sticker | 
                filters.animation | 
                filters.private | 
                ~filters.command(["start", "help", "donate", "d"]))
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

@bot.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    help_message = (
        "ᴊᴜsᴛ sᴀʏ 💬 ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ʜᴇʀᴇ❓\n\n"
        "➥ɪɴǫᴜɪʀʏ  🔦\n"
        "➥ᴅᴏᴜʙᴛs 🤔\n"
        "➦ᴘʀᴏʙʟᴇᴍs 😰\n"
        "➥ʜᴇʟᴘ 😟\n"
        "➥ꜰᴇᴇᴅʙᴀᴄᴋs 🔰\n"
        "➥ᴘʀᴏᴍᴏᴛɪᴏɴ 🛒\n"
        "[ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɢʀᴏᴜᴘ]\n"
        "➥ᴅᴏɴᴀᴛᴇ 💳 [ᴜs]\n\n"
        "🛠 ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs 🛠\n"
        "➥ /help\n"
        "➥ /donate\n"
        "➥ /settings\n\n"
        "ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❗️ @Anmol0700\n\n"
        "✧✧✧✧─ ｡ﾟ★: *.✦ .* :★. ─✧✧✧✧"
    )
    await message.reply_text(help_message, parse_mode="html")

@bot.on_message(filters.command(["donate", "d"]) & filters.private)
async def donate_command(_, message):
    text = """<b>❤️ᴛʜᴀɴᴋs ꜰᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ 😟

ᴅᴏɴᴀᴛᴇ ᴜs ᴛᴏ ᴋᴇᴇᴘ ᴏᴜʀ sᴇʀᴠɪᴄᴇs ᴄᴏɴᴛɪɴᴏᴜsʟʏ ᴀʟɪᴠᴇ 😢
ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴀɴʏ ᴀᴍᴏᴜɴᴛ 
ᴏꜰ 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ ...ᴀs ʏᴏᴜ ᴡɪsʜ 😊

📨 ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs 💳

ɢᴏᴏɢʟᴇᴘᴀʏ / ᴘᴀʏᴛᴍ / ᴘʜᴏɴᴘᴀʏ / ɴᴇᴛ ʙᴀɴᴋɪɴɢ ... 

❤️ꜰᴏʀ ᴅᴏɴᴀᴛɪᴏɴ ᴍᴇssᴀɢᴇ ᴍᴇ💬 
 👉 <i>@anmol0700</i> [or here via this bot]

ᴏʀ ʏᴏᴜ ᴄᴀɴ sᴄᴀɴ ᴛʜᴇ ǫʀ ᴄᴏᴅᴇ 👇
ᴜᴘɪ ʟɪɴᴋ 🔗 ᴀʟsᴏ ᴛʜᴇʀᴇ 😇
🌹 ᴛʜᴀɴᴋɪɴɢ ʏᴏᴜ 🌹</b>

🛍 UPI ID:</b> <code>anmol0700@fam</code>"""
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton('💳 ᴅᴏɴᴀᴛᴇ 💳', url='https://te.legra.ph/Donate-Us-03-15')
    ]])
    await message.reply_text(text=text, reply_markup=keyboard, parse_mode='html')

bot.start()
idle()
