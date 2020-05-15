"""Emoji
Available Commands:
.iaminnocentyaar
Credits to @iaminnocentyaar
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("iaminnocentyaar"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "iaminnocentyaar":
    await event.edit("@iaminnocentyaar")
    animation_chars = [
            "@iaminnocentyaar tera baap",
            "@iaminnocentyaar is bot ka creator",
            "mai mere malik @iaminnocentyaar kaeliye jaan de bhi sakta hu aur le bhi sakta hu",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@iaminnocentyaar"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
