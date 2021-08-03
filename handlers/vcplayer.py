from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""------------->Mᴜsɪᴄ•Pʟᴀʏᴇʀ<---------------
=>> *Song Playing* 🎧 
❍ /play <song name> - play song you requested
❍ /dplay <song name> - play song you requested via deezer
❍ /splay <song name> - play song you requested via jio saavn
❍ /playlist - Show now playing list
❍ /current - Show now playing
❍ /song <song name> - download songs you want quickly
❍ /search <query> - search videos on youtube with details
❍ /deezer <song name> - download songs you want quickly via deezer
❍ /saavn <song name> - download songs you want quickly via saavn
❍ /video <song name> - download videos you want quickly
=>> *Admins only*
❍ /player - open music player settings panel
❍ /pause - pause song play
❍ /resume - resume song play
❍ /skip - play next song
❍ /end - stop music play
❍ /userbotjoin - invite assistant to your chat
❍ /admincache - Refresh admin list
=>>   *Use*
1)  THIS BOT IS FOR PERSONAL USE
""",
        )
