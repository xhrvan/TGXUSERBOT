# Made by @xhrvan
# Don't remove these lines else gay..
# Kang with credits..


import asyncio

from TGXBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd("hdd"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 50)
    await event.edit("Happy Diwali Dosto🤗")
    animation_chars = [
        """-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙""",
        """💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
-#--💙happy💙diwali💙
#----💙happy💙diwali💙
#-----💙happy💙diwali💙
#-----💙happy💙diwali💙
#-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜""",
        """"💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖""",
        """❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙""",
        """💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️""",
        """💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚""",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd("diwali"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 20)
    await event.edit("❤Happy Diwali Dosto❤")
    animation_chars = [
        "💖happy💖diwali💖",
        "💙happy💙diwali💙",
        "❤️happy♥️diwali❤️",
        "💚happy💚diwali💚",
        "💜happy💜diwali💜",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])


@bot.on(admin_cmd("dosto"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 22)
    await event.edit("❤Dosto❤")
    animation_chars = [
        """💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜""",
        """ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""",
        """💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚                     💚💚
💚💚                     💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚
💚💚
💚💚
💚💚
💚💚""",
        """💛💛💛💛💛💛
💛💛💛💛💛💛💛
💛💛                💛💛
💛💛                💛💛
💛💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛
💛💛
💛💛
💛💛""",
        """💜💜                    💜💜
   💜💜              💜💜
      💜💜        💜💜
         💜💜  💜💜
            💜💜💜
              💜💜
              💜💜
              💜💜
              💜💜
              💜💜""",
        """💖💖💖💖💖💖💖
💖💖💖💖💖💖💖💖
💖💖                      💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                      💖💖
💖💖💖💖💖💖💖💖
💖💖💖💖💖💖💖""",
        """💝💝💝💝💝💝
💝💝💝💝💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
💝💝💝💝💝💝
💝💝💝💝💝💝""",
        """💖💖                               💖💖
💖💖                               💖💖
💖💖                               💖💖
💖💖                               💖💖
💖💖              💖            💖💖
 💖💖           💖💖          💖💖
 💖💖        💖💖💖       💖💖
  💖💖   💖💖  💖💖   💖💖
   💖💖💖💖      💖💖💖💖
    💖💖💖             💖💖💖""",
        """ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""",
        """💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘""",
        """💝💝💝💝💝💝
💝💝💝💝💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
💝💝💝💝💝💝
💝💝💝💝💝💝""",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 22])
CmdHelp("∂ιωαℓι").add_command(
        'hdd', None, 'µรε αɳ∂ รεε'
).add_command(
        'diwali', None, 'մsɾ αղժ sҽҽ'
).add()
