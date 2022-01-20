
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""Hᴇʏ Hᴏᴛᴛɪᴇ Sʜᴏᴛᴛɪᴇ, 
        I Aᴍ A Mᴜsɪᴄ Sᴇʀᴠᴇʀ Fᴏʀ Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Vᴏɪᴄᴇ Cʜᴀᴛ & Cʜᴀɴɴᴇʟs 😉🌸 Usᴇ Mᴇ Hᴀʀᴅʟʏ & Eɴᴊᴏʏ Mᴜsɪᴄ Wɪᴛʜ Sᴜᴘᴇʀ Dᴜᴘᴇʀ Qᴜᴀʟɪᴛʏ 😈❣️
Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : [𝐍 𝐢 𝐭 𝐫 𝐢 𝐜 𓆩👅𓆪](https://t.me/official_nitric).
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 ᴏᴡɴᴇʀ 🌸", url="https://t.me/Sanki_Owner")
                  ],[
                    InlineKeyboardButton(
                        "💡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Sanki_BOTs"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ 🎈", url="https://github.com/NitricXd/NanduMusic"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⁉️ ʜᴇʟᴘ ‼️", url="https://telegra.ph/N%E1%B4%80%C9%B4%E1%B4%85%E1%B4%9C-M%E1%B4%9Cs%C9%AA%E1%B4%84-S%E1%B4%87%CA%80%E1%B4%A0%E1%B4%87%CA%80-12-12"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""ɴᴀɴᴅᴜ's sᴇʀᴠᴇʀ ɪs ᴀʟɪᴠᴇ 😈""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Sanki_BOTs")
                ]
            ]
        )
   )
