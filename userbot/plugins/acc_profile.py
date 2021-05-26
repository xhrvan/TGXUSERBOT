"""Profile Updation Commands
.pbio <Bio>
.pname <Name>
.ppic"""
import os
from telethon import events
from telethon.tl import functions
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="pbio$"))
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest( 
            about=bio
        ))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:  
        await event.edit(str(e))

 
@bot.on(admin_cmd(pattern="pname$"))
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(functions.account.UpdateProfileRequest( 
            first_name=first_name,
            last_name=last_name
        ))
        await event.edit("My name was changed successfully")
    except Exception as e:  
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="ppic$"))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  
    photo = None
    try:
        photo = await borg.download_media( 
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY  
        )
    except Exception as e: 
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to Cloud ...")
            file = await borg.upload_file(photo) 
            try:
                await borg(functions.photos.UploadProfilePhotoRequest( 
                    file
                ))
            except Exception as e:  
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully changed")
    try:
        os.remove(photo)
    except Exception as e: 
        logger.warn(str(e)) 
CmdHelp("acc_profile").add_command(
       'pbio', '<reply to image>', 'use and see'
).add_command(
        'pname', '<reply to image>', 'use and see'
).add_command(
        'ppic', '<reply to image>', 'use and see'
).add()

