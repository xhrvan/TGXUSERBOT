
import asyncio
import random
from telethon import events
from TGXBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

# Thanks to LEGEND BRO.. 
# animation Idea by @xhrvan (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/46382df423d77941181f7.jpg"
file2="https://telegra.ph/file/46382df423d77941181f7.jpg"
file3="https://telegra.ph/file/46382df423d77941181f7.jpg"
file4="https://telegra.ph/file/46382df423d77941181f7.jpg"
file5="https://telegra.ph/file/46382df423d77941181f7.jpg"""" =======================CONSTANTS====================== """
pm_caption = "π₯Tgxbot is opπ₯\n\n"
pm_caption += "ππ **ππ¨π,πππ πππ ππππππππ , πππ ππΊππΎ πΌπΊππΎ ππΏ ππ π»πΎππππΎ .. πππππππ πππ ππΎππ πππΌππ«π.**ππ\n\n"
pm_caption += "ΰΌΰΌππΉAbout Me \n\n"
pm_caption += "π«π«**Tgxbot**π«π« >>γ 15.0.0\n"
pm_caption += "ππ**TGX**ππ   >>γ [Owner](https://t.me/itz_xhrvan)\n"
pm_caption += f"π°π°**πΈππππ**π°π°  >>γ {DEFAULTUSER}\n"
pm_caption += "β£β£ **Tgxbot**β£β£ >>γ [Group](https://t.me/Tgxbotz_chat)\n\n"
pm_caption += "ππ **Repo**ππ  >>γ [Repo](https://github.com/xhrvan/TGXBOT)\n\n"
pm_caption += "[β£πΉπ«ππ«πΉβ£](https://t.me/tgxbotz_chat)\n\n"
@borg.on(admin_cmd(pattern=r"abot"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    CmdHelp("Ξ±ΟΞΏΟ").add_command(
      'abot', None , 'BEST alive command'
).add()
