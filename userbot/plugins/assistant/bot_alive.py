from telethon import events
from . import *
from userbot import ALIVE_NAME
from userbot import bot
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"
PM_IMG = "https://telegra.ph/file/1038efe249510a9ef0588.jpg"
pm_caption = "➥ αssísԵαղԵ ís օղlíղҽ \n\n"
pm_caption += "➥ ѕγѕτєм ѕτατѕ\n"
pm_caption += "➥ τєℓєτнοи νєяѕιοи: `1.15.0` \n"
pm_caption += "➥ τgxϐοτ: `3.8.6` \n"
pm_caption += "➥ ∂αταϐαѕє ѕτατυѕ: `Functional`\n"
pm_caption += "➥ ϲυяяєиτ ϐяαиϲн: `master`\n"
pm_caption += f"➥ νєяѕιοи : `2.0`\n"
pm_caption += f"➥ мγ ϐοѕѕ: {DEFAULTUSER} \n"
pm_caption += "➥ нєяοκυ ∂αταϐαѕє: `AWS - Working Properly`\n\n"
pm_caption += "➥ **ℓιϲєиѕє** : [GNU General Public License v3.0](github.com/XHRVAN/TGXBOT/blob/master/LICENSE)\n"
pm_caption += "➥ ϲοργяιgнτ : By [τgxϐοτϲнατ](https://t.me/Tgxbotz_chat)\n"
pm_caption += "[Assistant By τgxϐοτυρ∂ατє](https://t.me/tgxbotz_update)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
