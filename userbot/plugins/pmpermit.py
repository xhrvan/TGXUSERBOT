import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT, LEGEND_ID
from userbot.Config import Config
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp


PM_TRUE_FALSE = Config.PM_DATA

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
LEGENDPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/7b2fefb2c78c90734444d.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
LEGEND = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n THIS IS ILLEGAL AND REGARDED AS CRIME"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"
USER_BOT_WARN_ZERO = "**Hello Sir/Miss, ʏᴏᴜ ᴅɪᴅ'ɴᴛ sᴇᴇ ᴡʜᴀᴛ ɪ sᴀɪᴅ ᴍʏ ᴍᴀsᴛᴇʀ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴏғғʟɪɴᴇ ᴅᴏɴᴛ sᴘᴀᴍ.`\n**ɴᴏᴡ sʜᴜᴛ ᴜᴘ.... ᴀɴᴅ ɢᴇᴛ ʟᴏsᴛ**"
USER_BOT_NO_WARN =(
    "__Hello Sir/Miss,Im Here To Protect.Dont Under Estimate Me 😂😂.__This is **LEGENDBOT Ultra Private Security Guard H hum Give ur identity before msg my master 😎⚠️**.\n"
    f"This is my master {DEFAULTUSER}'s Inbox\n"
    f"\n**{LEGEND}**\n\n"
    f"{DEFAULTUSER}'s `sᴏʀʀʏ, ɪ ᴅᴏɴᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴘᴇᴏᴘʟᴇ ᴀʀᴇ sᴏ ғʀᴇᴇ ᴛʜᴀᴛ ᴛʜᴇʏ ɢᴇᴛ ᴛʜᴇ ᴛɪᴍᴇ ᴛᴏ ᴅᴏ ᴜsᴇʟᴇss ᴄʜᴀᴛs sᴇᴇ ᴍʏ ᴍᴀsᴛᴇʀ's ɪɴʙᴏx ɪᴛ ɪs ғɪʟʟᴇᴅ ᴡɪᴛʜ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴍᴀɪʟs ɢᴏ ᴀɴᴅ ᴅᴏ ʏᴏᴜʀ ᴡᴏʀᴋ ᴅᴏɴ'ᴛ ᴅɪsᴛᴜʀʙ ᴍʏ ᴍᴀsᴛᴇʀ...\n"
                    "ɪғ ɪᴛ ɪs ᴜʀɢᴇɴᴛ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ ,ᴅᴇsᴄɪᴘᴛɪᴏɴ ᴀɴᴅ ʀᴇᴀsᴏɴ...ᴀɴᴅ ɪ ʜᴏᴘᴇ ɪғ ʏᴏᴜ ᴀʀᴇ ᴀ ɢᴏᴏᴅ ᴘᴇʀsᴏɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ʀᴇᴘʟʏ ʙᴜᴛ ɪ ᴀᴍ ɴᴏᴛ sᴜʀᴇ ᴀʙᴏᴜᴛ ᴛʜᴀᴛ`\n\n"
    "To start a valid conversation\n🔱Register Your Request!🔱\nSend `/start` To Register Your Request\nHopefully u will get a reply🔥"
)

if Var.PRIVATE_GROUP_ID is not None:

@bot.on(admin_cmd(pattern="block$"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    if event.is_private:
        replied_user = await event.client(GetFullUserRequest(await event.get_input_chat()))
        firstname = replied_user.user.first_name
        if str(event.chat_id) in DEVLIST:
            await event.edit("**I can't block my creator !!**")
            return
        if pm_sql.is_approved(event.chat_id):
            pm_sql.disapprove(event.chat_id)
        await event.edit("Go Get Some Sleep Retard !! \n\n**Blocked** [{}](tg://user?id={})".format(firstname, event.chat_id))
        await event.client(functions.contacts.BlockRequest(event.chat_id))
    elif event.is_group:
        reply_s = await event.get_reply_message()
        if not reply_s:
            await eod(event, "Reply to someone to block them..")
            return
        replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
        firstname = replied_user.user.first_name
        if str(reply_s.sender_id) in DEVLIST:
            await event.edit("**I can't Block My Creator !!**")
            return
        if pm_sql.is_approved(event.chat_id):
            pm_sql.disapprove(event.chat_id)
        await event.edit("Go fuck yourself !! \n\n**Blocked** [{}](tg://user?id={})".format(firstname, reply_s.sender_id))
        await event.client(functions.contacts.BlockRequest(reply_s.sender_id))
        await asyncio.sleep(3)
        await event.delete()
        
        
if PM_ON_OFF != "DISABLE":
    @bot.on(events.NewMessage(outgoing=True))
    async def auto_approve_for_out_going(event):
        if event.fwd_from:
            return
        if not event.is_private:
            return
        chat_ids = event.chat_id
        sender = await event.client(GetFullUserRequest(await event.get_input_chat()))
        first_name = sender.user.first_name
        if chat_ids == bot.uid:
            return
        if sender.user.bot:
            return
        if sender.user.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if str(event.chat_id) in DEVLIST:
            return
        if not pm_sql.is_approved(event.chat_id):
            if not event.chat_id in PM_WARNS:
                pm_sql.approve(event.chat_id, "outgoing")
                
    @bot.on(LEGEND_cmd(pattern="(a|approve|allow)$"))
    async def approve(event):
        if event.fwd_from:
            return
        if event.is_private:
            replied_user = await event.client(GetFullUserRequest(await event.get_input_chat()))
            firstname = replied_user.user.first_name
            if not pm_sql.is_approved(event.chat_id):
                if event.chat_id in PM_WARNS:
                    del PM_WARNS[event.chat_id]
                if event.chat_id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[event.chat_id].delete()
                    del PREV_REPLY_MESSAGE[event.chat_id]
                pm_sql.approve(event.chat_id, "Approved")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, event.chat_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif pm_sql.is_approved(event.chat_id):
                hel_ = await event.edit('Already In Approved List!!')
                await asyncio.sleep(3)
                await hel_.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('Reply to someone to approve them !!')
                return
            if not pm_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pm_sql.approve(reply_s.sender_id, "Approved")
                await event.edit(
                        "Approved to pm [{}](tg://user?id={})".format(firstname, reply_s.sender_id)
                    )
                await asyncio.sleep(3)
                await event.delete()
            elif pm_sql.is_approved(reply_s.sender_id):
                await event.edit('User Already Approved !')
                await event.delete()

    @bot.on(LEGEND_cmd(pattern="(da|disapprove|disallow)$"))
    async def dapprove(event):
        if event.fwd_from:
            return
        if event.is_private:
            replied_user = await event.client(GetFullUserRequest(await event.get_input_chat()))
            firstname = replied_user.user.first_name
            if str(event.chat_id) in DEVLIST:
                await event.edit("**Unable to disapprove this user. Seems like God !!**")
                return
            if pm_sql.is_approved(event.chat_id):
                pm_sql.disapprove(event.chat_id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, event.chat_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pm_sql.is_approved(event.chat_id):
                led = await event.edit("I don't think he was approved !!")
                await asyncio.sleep(3)
                await led.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit("Reply to someone to Disapprove them !!")
                return
            if str(reply_s.sender_id) in DEVLIST:
                await event.edit("**Unable to disapprove this user. Seems like God !!**")
                return
            if pm_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pm_sql.disapprove(reply_s.sender_id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, reply_s.sender_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pm_sql.is_approved(reply_s.sender_id):
                await event.edit('Not even in my approved list.')
                await event.delete()    
                
                
    @bot.on(LEGEND_cmd(pattern="listapproved$"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pm_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if not event.is_private:
            return
        if event.sender_id == bot.uid:
            return
        if str(event.sender_id) in DEVLIST:
            return
        if Config.LOGGER_ID is None:
            await bot.send_message(bot.uid, "Please Set `LOGGER_ID` For Working Of Pm Permit")
            return
        message_text = event.message.raw_text
        chat_ids = event.sender_id
        if HELL_FIRST == message_text:
            return
        sender = await event.client.get_entity(await event.get_input_chat())
        if chat_ids == bot.uid:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if pm_sql.is_approved(chat_ids):
            return
        if not pm_sql.is_approved(chat_ids):
            await do_pm_permit_action(chat_ids, event)
                                       
    async def do_pm_permit_action(chat_ids, event):
        if chat_ids not in PM_WARNS:
            PM_WARNS.update({chat_ids: 0})
        if PM_WARNS[chat_ids] == 3:
            r = await event.reply(HELL_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_ids].delete()
            PREV_REPLY_MESSAGE[chat_ids] = r
            the_message = ""
            the_message += "#BLOCK\n\n"
            the_message += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
            the_message += f"Message Counts: {PM_WARNS[chat_ids]}\n"
            try:
                await bot.send_message(
                    entity=Config.LOGGER_ID,
                    message=the_message,
                    link_preview=False,
                    silent=True,
                )
                return
            except BaseException:
                pass
        
        botusername = Config.BOT_USERNAME
        tap = await bot.inline_query(botusername, "pm_warn")
        hel_ = await tap[0].click(event.chat_id)
        PM_WARNS[chat_ids] += 1
        if chat_ids in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_ids].delete()
        PREV_REPLY_MESSAGE[chat_ids] = hel_

CmdHelp("pm_permit").add_command(
  "allow", "<in pm>", "Approves the user in which pm cmd is used."
).add_command(
  "disallow", "<in pm>", "Disapprove User to PM you."
).add_command(
  "block", "<in pm>", "Blocks the user"
).add_command(
  "listapproved", None, "Sends the list of all users approved by Hêllẞø†"
).add_info(
  "PM SECURITY"
).add_warning(
  "✅ Harmless Module."
).add()
