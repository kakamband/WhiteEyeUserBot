# @TheShubhendra (shubhendrakushwaha94@gmail.com)

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

@WhiteEye.on(WhiteEye_on_cmd(pattern=r"getall$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    text = "`First Name| Last Name | Username | Id`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 200):
        text += f"\n**{x.first_name} | {x.last_name}** | @{x.username} | {x.id}"
    await event.edit(text)


CMD_HELP.update(
    {
        "getall": "**GetAll**\
\n\n**Syntax : **`.getall <reply to a user / mention their ID>`\
\n**Usage :** Gives You All Info About That User."
    }
)
