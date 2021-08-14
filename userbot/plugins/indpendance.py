import asyncio
from userbot import *
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"


@borg.on(admin_cmd(pattern="indpendance$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 6
    animation_ttl = range(0, 17)
    await event.edit("Starting...")
    animation_chars = [
        "**Hello!👋**",
        "**How Are You?**",
        f"**{DEFAULTUSER}ᕼᗩᑭᑭᎩ ᏆᑎᗞᑭᗴᑎᗞᗩᑎᑕᗴᗞᗩᎩ**"
        "ᗯᏆᔑᕼᏆᑎᏀ ᑌ ᕼᗩᑭᑭᎩ Ꮖᑎᗞᑭᗴᑎᗞᗩᑎᑕᗴ ᗞᗩᎩ",
        "**Wishing you 👈 a 👌 day 🌞 filled 😏 with 👏 happiness and 👏 a 👌 year 🎉 filled 😏 with 👏 joy 😁.**",
        "**Sending you 👈 smiles 😀 for  every 👏 moment 🏆 of your special 😲 day 🌞*",
        "**Have 👏 a 👌 wonderful 😊 time 🕐 and a very 👌 happy 😊 Indpendanc Day!**",
        "**Count your 👏 life 👤 by 😈 smiles, 😀 not 🚫 tears. 😭 Count your 👏 age 👵 by 😈 friends, 👫 not 🚫 years. 📅 Happy 😊 Indpendance Day!**",
        "**From every mountain side Let Fredom Ring**",
        "**Independence means.. enjoying freedom and empowering others too to let them do so.**",
        "ͲϴᎠᎪᎽ ᏔᎬ ᎪᎡᎬ ҒᎡᎬᎬ ᏴᎬᏟᎪႮՏᎬ ᎷᎪΝᎽ ՏᎪᏟᎡᏆҒᏆᏟᎬᎠ ͲᎻᎬᎡᎬ ᏞᏆᏙᎬՏ ҒϴᎡ ᏆΝᎠᏆᎪ \nՏᎪᏞႮͲᎬ ͲᎻᎬ ᏀᎡᎬᎪͲ ՏϴႮᏞՏ",
        "[Visit It](https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg)",
        "[ᎻᎪᏢᏢᎽ ᏆΝᎠᏢᎬΝᎠᎪΝᏟᎬ ᎠᎪᎽ](https://t.me/Legend_Userbot)",
    ]
    for i in animation_ttl:  # By @Legend_Mr_Hacker LegendBot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 
CmdHelp("indpendance").add_command(
    'indpendance', None, 'Happy Indpendance Day'
).add()
