import re

from LEGENDBOT import bot
from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from LEGENDBOT.cmdhelp import CmdHelp
from LEGENDBOT.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(aura):
    LEGEND = aura.pattern_match.group(1)
    if not LEGEND:
        if aura.is_reply:
            (await aura.get_reply_message()).message
        else:
            await edit_or_reply(aura, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(LEGEND))}")

    await troll[0].click(
        aura.chat_id,
        reply_to=aura.reply_to_msg_id,
        silent=True if aura.is_reply else False,
        hide_via=True,
    )
    await aura.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
