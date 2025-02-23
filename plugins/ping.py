# UserBot
# Copyright (C) 2021-2023 Teamx-cloner 
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_bot")

import asyncio
import os
import sys
import time
from telethon import events, TelegramClient
from telethon.tl.functions import PingRequest
from secrets import choice
from telethon import Button
from pyUltroid._misc import sudoers
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos
from pyUltroid.fns.custom_markdown import CustomMarkdown
from pyUltroid.fns.helper import download_file, inline_mention
from ._inline import *
from . import (
OWNER_NAME,
OWNER_ID,
BOT_NAME,
OWNER_USERNAME,
asst,
start_time,
time_formatter,
udB,
ultroid_cmd as xteam_cmd,
get_string,
ultroid_bot as client,
eor,
ultroid_bot,
call_back,
callback,
Button,
)

PING = [
    [  # First row of buttons (you can have multiple rows)
            #InlineKeyboardButton("Button 1 Text", url="https://example.com/1"),  # Example URL button
            Button.inline("CLOSE", data="close"),
        #InlineKeyboardButton("ᴘɪɴɢ", callback_data="close") # Example callback button
        ]
]

#markup = ReplyInlineMarkup(PING)


@callback(data="close", owner=True)
async def on_plug_in_callback_query_handler(event):
    await event.edit(
        get_string("inline_5"),
        buttons=Button.inline("OPEN", data="open"),
    )

async def mention_user(user_id):
    try:
        user_entity = await ultroid_bot.get_entity(user_id)
        first_name = user_entity.first_name
        mention_text = f"[{first_name}](tg://user?id={user_id})"
        return mention_text
    except Exception as e:
        print(f"Failed to mention user: {e}")


@xteam_cmd(pattern="ping$", chats=[], type=["official", "assistant"])
async def _(event):
    start = time.time()
    x = await event.reply("Ping!")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    await x.edit(f"**Pong!\n{end}ms**")


"""
papnya = [
        pap
        async for pap in e.client.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
        )
    ]

ppcpnya = [
        ppcp
        async for ppcp in event.client.iter_messages(
            "@ppcpcilik", filter=InputMessagesFilterPhotos
        )
    ]

desahcewe = [
        desah
        async for desah in event.client.iter_messages(
            "@desahancewesangesange", filter=InputMessagesFilterVoice
        )
    ]
"""
@xteam_cmd(pattern="Cping")
async def wping(e):
    asupannya = [
        asupan
        async for asupan in e.client.iter_messages(
            "@xcryasupan", filter=InputMessagesFilterVideo
        )
    ]
    start = time.time()
    x = await e.eor("Pong!")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    #await asyncio.sleep(1)
    try:
       await client.send_message(
    e.chat.id,
    f"<blockquote> Ping : {end}ms\nUptime : {uptime}\nOwner :{OWNER_NAME}</blockquote>",
    parse_mode="html",
    buttons=PING,
    file=choice(asupannya),
       )
   #x = await client.send_message(e.chat.id, "<blockquote> **Ping :** `{end}ms`\n**Uptime :** `{uptime}`\n**Owner** :`{OWNER_NAME}`</blockquote>", parse_mode="html", file=choice(asupannya))")
        #await x.edit(get_string("ping").format(f"[{BOT_NAME}](https://t.me/{asst.username})", end, uptime, f"{inline_mention(ultroid_bot.me)}"), file=choice(asupannya), buttons=PING)
        #await x.edit(f"**Ping :** `{end}ms`\n**Uptime :** `{uptime}`\n**Owner** :`{OWNER_NAME}`", file=choice(asupannya))
    except Exception as e:
        await x.edit(f"**Ping Error:** {e}")

@xteam_cmd("cping$", devs=True)
async def _(e):
    start = time.time()
    x = await e.eor("Pong!")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    user = await e.client.get_sudoers()
    message = "**✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧**\n\n✧ **ᴘɪɴɢᴇʀ :** `{} ms`\n✧ **ᴜᴘᴛɪᴍᴇ :** `{}`\n✧ **ᴏᴡɴᴇʀ :** `{}`\n✧ **ɪᴅ :** `{}`"
    await e.reply(
        message.format(
            duration,
            uptime,
            user.first_name,
            user.id
        )
)
