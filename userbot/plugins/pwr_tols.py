 
import os
import sys
import asyncio
from os import execl
from time import sleep

from TGXBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import HEROKU_APP, bot

@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Restarting **[ βββ ]** ...\nType `.ping` or `.help` to check if I am working π")
    await event.edit("Restarting **[ βββ ]** ...\nType `.ping` or `.help` to check if I am working π")
    await event.edit("Restarting **[ βββ ]** ...\nType `.ping` or `.help` to check if I am working π")
    await event.edit("Restarting **[ βββ ]** ...\nType `.ping` or `.help` to check if I am working π")
    await event.edit("Restarted TgxBot Ξ½2.ΞΏ**[ β ]** ...\nType `.ping` or `.help` after 10min to check if I am working π")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `Turning off bot now ... Manually turn me on later or follow step of update in @Tgxbotz_chat` ΰ² _ΰ² ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


CmdHelp("ΟΟΡ ΟΞΏβΡ").add_command(
  "restart", None, "Restarts your userbot. ReΡtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add()
