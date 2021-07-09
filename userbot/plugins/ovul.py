
import random
import re
from . import *
from userbot.cmdhelp import CmdHelp

uwus = [
    "(・`ω´・)",
    "UwU",
    "uwu",
    "OwO",
    "owo",
    "(●__●)",
    "(゜o゜;",
    "⊙.☉",
    "(ô_ô)",
    "~:o",
    "¶-¶",
    "(*^*)",
    "(•_•)",
    "(⑉⊙ȏ⊙)",
    "*(^O^)*",
    "(°_°)",
]

@bot.on(admin_cmd( pattern="ovul"))
async def faces(ult):
    uff = random.choice(uwus)
    return await ult.edit(f"{uff}")
    
    

CmdHelp("ovul").add_command(
'ovul', None, 'Use and See'
).add()
