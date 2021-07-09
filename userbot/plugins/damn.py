from . import *
damn = [
"╔═══╗",
"╚╗╔╗║",
"─║║║╠══╦╗╔╦═╗",
"─║║║║╔╗║╚╝║╔╗╗",
"╔╝╚╝║╔╗║║║║║║║",
"╚═══╩╝╚╩╩╩╩╝╚╝"
]
@bot.on(admin_cmd(pattern="damn")
async def sorryy(ult):
  return await eor(ult,"\n".join(damn))
CmdHelp("damn").add_command(
'damn', None, 'In animation'
).add()
