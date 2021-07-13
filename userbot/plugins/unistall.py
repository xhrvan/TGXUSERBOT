
from telethon import events
from userbot.events import remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
from userbot import LOAD_PLUG
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd, sudo_cmd
import os
@bot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path =f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"Uninstalled {shortname} successfully By Legendbot")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))
from userbot.cmdhelp import CmdHelp
CmdHelp("unistall").add_command(
  'unistall <plugin name>', None, 'Its help to unistall plugin'
).add()
