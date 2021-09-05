from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from . import *
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module, start_assistant
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")

hl = Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/75e1eda1498620f0030ea.jpg"



LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)

print(f"""『τgxυѕєяϐοτ』➙𖤍࿐ ιѕ οи!!! τgxϐοτνєяѕιοи :- {LEGENDversion}
TYPE :- " .gpromote @xhrvan " OR .help OR .ping CHECK IF I'M ON!
╔════❰TGXBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - Itz_xhrvan
║┣⪼{LEGEND_PIC}
║┣⪼ CREATOR -@Tgxbotz
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨τgxυѕєяϐοτ✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")


    try:
        await bot(JoinChannelRequest("@Its_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Legend_Userbot"))
    except BaseException:
         pass


bot.loop.create_task(legend_is_on())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
