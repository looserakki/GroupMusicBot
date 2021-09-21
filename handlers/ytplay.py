import os
from os import path
import requests
import aiohttp
import youtube_dl
from pyrogram import Client
from pyrogram.types import Message, Voice
from youtube_search import YoutubeSearch
from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command"play") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐃𝐢𝐫𝐞𝐜𝐭 𝐏𝐥𝐚𝐲 𝐅𝐫𝐨𝐦 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐒𝐞𝐫𝐯𝐞𝐫")
    sender_id = message.from_user.id
    user_id = message.from_user.id
    sender_name = message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    await lel.edit("𝐅𝐨𝐮𝐧𝐝 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐏𝐥𝐚𝐲𝐞𝐫")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        lel.edit(
            "❌𝐒𝐨𝐧𝐠 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 𝐎𝐧 𝐘𝐨𝐮𝐓𝐮𝐛𝐞.𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐡𝐞𝐜𝐤 𝐘𝐨𝐮𝐫 𝐒𝐩𝐞𝐥𝐥 𝐎𝐫 𝐓𝐫𝐲 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 𝐨𝐧𝐞 "
        )
        print(str(e))
        return

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐖𝐚𝐭𝐜𝐡 𝐎𝐧 𝐘𝐨𝐮𝐭𝐮𝐛𝐞🎬",
                        url=f"{url}"),
                    InlineKeyboardButton(
                        text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭📢",
                        url="https://t.me/DeCodeSupport"),
                ],
                [
                    InlineKeyboardButton(
                        text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥🤔",
                        url="t.me/DeeCodeBots"),
                    InlineKeyboardButton(
                        text="𝐎𝐰𝐧𝐞𝐫❤️",
                        url="https://t.me/About_Blaze"),
                ]
            ]
        )

    keyboard2 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐖𝐚𝐭𝐜𝐡 𝐎𝐧 𝐘𝐨𝐮𝐭𝐮𝐛𝐞",
                        url=f"{url}"),
                    InlineKeyboardButton(
                        text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥",
                        url="t.me/TgBotzXD"),
                ],
                
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None

    if audio:
        await lel.edit_text("Lel")

    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return  lel.edit_text("➕𝐆𝐢𝐯𝐞 𝐀𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐄𝐥𝐬𝐞 𝐅𝐮𝐜𝐤 𝐎𝐟𝐟")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=thumb_name, 
        caption=f"#⃣➕ 𝐒𝐨𝐧𝐠 𝐀𝐝𝐝𝐞𝐝 𝐓𝐨 𝐐𝐮𝐞𝐮𝐞 𝐀𝐭 𝐏𝐨𝐬𝐢𝐭𝐢𝐨𝐧 {position}!",
        reply_markup=keyboard2)
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo=thumb_name,
        reply_markup=keyboard,
        caption="▶️ **𝐏𝐥𝐚𝐲𝐢𝐧𝐠** 𝐇𝐞𝐫𝐞 𝐓𝐡𝐞 𝐒𝐨𝐧𝐠 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲 {}  ".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
