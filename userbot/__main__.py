from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module, start_assistant
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import telethon.utils
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
os.system("pip install -U telethon")

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.TG_BOT_USER_NAME_BF_HER is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        LOGS.info("Checking Completed. Proceeding to next step...")
        LOGS.info("🔰 Starting LEGENDBOT 🔰")
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
        LOGS.info("🔥 LEGENDBOT Startup Completed 🔥")
    except Exception as e:
        LOGS.error(f"TG_BOT_TOKEN_BF_HER - {str(e)}")
        sys.exit()
        
import glob
if LOAD_USERBOT == True:
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
           
  else:
    print("Userbot is Not Loading As U Have Disabled")
       
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

import userbot._core

# Join Feds Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Legend_Mr_Fed"))
    except BaseException:
        pass

# Why not come here and chat??
    try:
        await bot(JoinChannelRequest("@Legend_Mr_Feds"))
    except BaseException:
        pass


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info(
    "⚡ Your LEGENDBOT Is Now Working ⚡"
)
print(f"""LEGENDBOT IS ON!!! LEGENDBOT VERSION :- {LEGENDversion}
CONTACT @LEGEND_MR_HACKER
OWNER :- @Legend_Mr_Hacker
CREATOR :- @Legend_Mr_Hacker
DO .op OR .ping OR .legend CHECK IF I'M ON!
IF YOU FACE ANY ISSUE THEN ASK WITH @Legend_Mr_Hacker.""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
