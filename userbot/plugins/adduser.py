"""Add the user(s) to the current chat
Syntax: .edd <User(s)>"""
import asyncioimport iofrom asyncio import sleepfrom datetime import datetimefrom math import sqrtfrom telethon.errors import ( ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, ChatAdminRequiredError, UserAdminInvalidError,)from telethon.tl import functionsfrom telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequestfrom telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequestfrom telethon.tl.types import ( ChannelParticipantAdmin, ChannelParticipantCreator, ChannelParticipantsAdmins, ChannelParticipantsBots, ChannelParticipantsKicked, ChatBannedRights, MessageActionChannelMigrateFrom, UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently,)from telethon.utils import get_input_location from userbot import BOTLOG, BOTLOG_CHATID from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_replyfrom userbot.cmdhelp import CmdHelpfrom userbot.Config import Config


@borg.on(admin_cmd(pattern="edd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.add` users to a chat, don't use this in PM")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Added Successfully")
        else:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("ADDED the user to the chat successfully.")
