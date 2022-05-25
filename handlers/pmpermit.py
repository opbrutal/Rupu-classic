from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"ʜɪ ᴛʜɪs ᴀᴄᴄᴏᴜɴᴛ ɪs ᴍᴀɴᴀɢɪɴɢ ʙʏ @b_4_brutal_official ᴀɴᴅ ᴅᴏɴᴛ ᴅɪsʙᴜʀsᴇ ᴏᴡɴᴇʀ..❣️")
  return                        
