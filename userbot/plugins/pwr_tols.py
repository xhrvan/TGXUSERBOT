 
import os
import sys
import asyncio
from os import execl
from time import sleep

from TGXBOT.utils import admin_cmd
from smartbot.cmdhelp import CmdHelp
from smartbot import HEROKU_APP, bot

@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Restarting **[ ░░░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ █░░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ ██░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ ███ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarted TgxBot ν2.ο**[ ✓ ]** ...\nType `.ping` or `.help` after 10min to check if I am working 🙂")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `Turning off bot now ... Manually turn me on later or follow step of update in @Tgxbotz_chat` ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["smartbot"].scale(0)
    else:
        sys.exit(0)


CmdHelp("ρωя τοℓѕ").add_command(
  "restart", None, "Restarts your smartbot. Reѕtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add()
