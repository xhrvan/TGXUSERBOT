import random
from . import *
sorry = ["I'm Sorry （｡≧ _ ≦｡）","≦(._.)≧ : Sorry","o(´д｀o) : I'm Sorry Pleaze Forgive me","Sorry ヾ(_ _*)","(๑•́ㅿ•̀๑ ) ᔆᵒʳʳᵞ","Sorry:(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ","༒ᎦᎧᏒᏒⲨ☆ʝααи༒"]
@ultroid_cmd(pattern="sorry")
async def _(event):
  s = random.choice(sorry)
  return await event.edit(f"{s}")



CmdHelp("sorry").add_command(
  'sorry', None, 'Use and See')
