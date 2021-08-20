import time

from telethon import version
from smartbot import ALIVE_NAME, StartTime, LEGENDversion
from TGXBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from smartbot.cmdhelp import CmdHelp

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "TGXBOT"
LEGEND_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "LEGEND CHOICE LEGENDBOT"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        LEGEND_caption += f"┏━━━━━нєγ! ι αм αℓινє━━━━━━\n"
        LEGEND_caption += f"┣ νєяѕιοи - 0.2\n"
        LEGEND_caption += f"┣ ργτнοи - 3.9.5\n"
        LEGEND_caption += f"┣ ϐяαиϲн - main\n"
        LEGEND_caption += f"┣ τєℓєτнοи - `{version.__version__}`\n"
        LEGEND_caption += f"┣ υρτιмє - `{uptime}`\n"
        LEGEND_caption += f"┗━━━━━━━[τgxυѕєяϐοτ](t.me/tgxbotz)━━━━━━━━\n"
           

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"┏━━━━━нєγ! ι αм αℓινє━━━━━━\n"
            f"┣ υρτιмє - `{uptime}`\n"
            f"┣ τєℓєτнοи - `{version.__version__}`\n"
            f"┣ νєяѕιοи - 0.2`\n"
            f"┣ ργτнοи - 3.9.5`\n"
            f"┣ ϐяαиϲн -  main \n"
            f"┗━━━━━━━τgxυѕєяϐοτ━━━━━━━━\n"
        )

CmdHelp("ɓσƭรƭαƭµร").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add()
