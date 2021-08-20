# (c) @smartbot
# Original written by @smartbot edit by @I_m_Rock

import asyncio
from collections import deque

from smartbot.utils import admin_cmd
from smartbot.cmdhelp import CmdHelp
CmdHelp("earth").add_command(
   'earth', None, 'animation'
).add()

@borg.on(admin_cmd(pattern="earth"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
