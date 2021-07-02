
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from LEGENDBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import version, events
from math import ceil
from telethon.events import NewMessage
from telethin.tl.custom import dialog
from telethon.tl.types import channel, chat, user
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PIC
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/ba75256278e8ab0cd521e.jpg"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

   pm_caption += f"**🔱LEGENDBOT IS Awake🔱**\n"
   pm_caption += f"**My Bot Status**\n\n\n"
   pm_caption += f"Telethon: TELETHON-1.19.0 \n\n"
   pm_caption += f"Python: PYTHON-3.8.5 \n\n"
   pm_caption += f"I'll Be With You Master Till My Dyno Ends!!☠ \n\n"
   pm_caption += f"OWNER` : @Legend_Mr_Hacker\n\n"
   pm_caption += f"MY BOSS😊: {DEFAULTUSER}\n\n"
                
            
#@command(outgoing=True, pattern="^.awake$")
@bot.on(admin_cmd(pattern=r"awake"))
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await bot.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
    
    
CmdHelp("awake").add_command(
  'awake', None, 'Awake Or Not'
).add()
