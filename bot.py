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
from pyrogram import Client, filters, idle
from sample_config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from etc.sql.user import get_userid

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
       return await message.reply_text(f"Hey there, I am PM Bot of {Config.OWNER_USERNAME}. You can send your message here!")

@bot.on_message(filters.text | 
                filters.media | 
                filters.sticker | 
                filters.animation | 
                filters.private | 
                ~filters.command("start"))
async def send_func(_, message):
    userid = message.from_user.id
    if userid == Config.OWNER_ID:
       if message.reply_to_message:
          msg = message.reply_to_message
          user_id, reply_message_id = get_userid(msg.id)
          try:
              await bot.send_message(user_id, reply_to_message_id = reply_message_id)
          except Exception as e:
              return await message.reply(str(e))
    else:
         try:
             await message.forward(Config.OWNER_ID)
         except:
             return
    
  
bot.start()
idle()
