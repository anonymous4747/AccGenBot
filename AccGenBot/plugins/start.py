from AccGenBot import AccGen
from telethon import events, Button
from AccGenBot.verify import verify
from Configs import Config

@AccGen.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    await AccGen.send_message(Config.LOGS_CHAT, f"Bot Started By [{event.sender.first_name}](tg://user?id={event.sender_id}).")
    check = await verify(Config.CHANNEL_US, event, AccGen)
    check2 = await verify('@DynamicCoderZ', event, AccGen)
    if check and check2 is False:
       await event.reply("**Join my channel to use me:)**", buttons=[
       [Button.url("Join Channel",url="https://t.me/DynamicCoderZ)]
       [Button.url("Configs Channel",url="https://t.me/ConfigsByHackerSploit)]
       ])
       return

    if event.is_group:
       await event.reply("**Sorry, I Work in PM only.**\n__I am leaving this chat...__")
       await AccGen.delete_dialog(event.chat_id)
       return

    START_TEXT = """
**Heya {}**
Welcome to AccGen from here you can generate
the accounts you want
Press the button below for starting
""".format(event.sender.first_name)

    await event.reply(START_TEXT, buttons=[
    [Button.inline("Generate Accounts", data="gen")],
    [Button.url("JOIN CHANNEL", "https://t.me/ConfigsByHackerSploit")]
    ])
