from AccGenBot import AccGen
from AccGenBot.verify import verify
from telethon import events, Button
from Configs import Config

@AccGen.on(events.callbackquery.CallbackQuery(data="gen"))
async def gen(gen):
     check = await verify(Config.CHANNEL_US, gen, AccGen)
     if check and check2 is False:
       await gen.reply("**please Join my channel to use me:)**", buttons=[
       [Button.url("Join Channel",url="https://t.me/ConfigsByHackerSploit)]
       [Button.url("Bots Channel", url="https://t.me/DynamicCoderZ")]
       ])
       return

     TEXT = """
**Heya {}**
Choose the account you wanna generate.
""".format(gen.sender.first_name)

     await gen.edit(TEXT, buttons=[
     [Button.inline("Zee5", data="zee5"), Button.inline("Voot", data="voot")],
     [Button.inline("AltBalaji", data="alt"), Button.inline("Spotify", data="sp")],
     [Button.inline("Crunchyroll",data="crunchy")]
     ])
