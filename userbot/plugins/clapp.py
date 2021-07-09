import asyncio
from . import *
@bot.on(admin_cmd(pattern="clapp"))
async def clap(ult):
  await ult.edit("👐👏👐👏 👐👏")
  await asyncio.sleep(1)
  await ult.edit("👐👏👐👏👐👏👐")
CmdHelp("clapp").add_command(
'clapp', None, 'Use and See'
).add()
