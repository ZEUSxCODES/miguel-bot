#    Copyright (C) 2021 by @ImJanindu
#    This programme is a part of Infinity Bots
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging
from pyrogram import Client, filters
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
       return await message.reply_text("**Your assistant is online sir!**")
    else:
       return await message.reply_text(f"Hey there, I am assistant chatbot of {Config.OWNER_USERNAME}. You can send your message here, I'll send your message to him!")

@bot.on_message(filters.text | filters.media | filters.sticker | filters.animation & ~filters.user(Config.OWNER_ID))
async def send_func(_, message):
    await bot.forward_messages(Config.OWNER_ID, message_ids=message.message_id)
    
  
bot.start()
