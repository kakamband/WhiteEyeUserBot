import time
from datetime import datetime

import pytz
from WhiteEyeUserBot import bot

UpdatesChannel = "WhiteEyeBots"
Botsz = [
    "WhiteEyeRenameBot",
    "WhiteEyeURLUploaderBot",
    "WhiteEyeTelegraphBot",
    "WhiteEyeLinkToFileBot",
    "WhiteEyeSubtitleBot",
    "WhiteEyeYouTubeBot",
    "WhiteEyeForceSubscriberBot",
    "WhiteEyeGDrivebot",
    "WhiteEyeTagRemoverBot",
    "WhiteEyeDeleteAllBot",
    "WhiteEyeCompressorBot",
    "Miss_ArantxaBot",
    "WhiteEyeURLShortnerBot",
    "FilmsRequestBot",
]


@assistant_cmd("botlist", is_args=True)
async def bots(event):
    first_msg = "<b>List Of All Bots And Working Status In @WhiteEyeBots</b>\n_______________________________</b>\n\n"
    reply = await event.reply(first_msg, parse_mode="html")
    Listed = Botsz
    for bot in Listed:
        checking = f"<b>☘️ @{bot} Status : Checking...♻️</b>\n\n"
        first_msg += checking
        await reply.edit(first_msg, parse_mode="html")
        snt = await bot.send_message(bot, "/start")
        time.sleep(5)
        msg = await bot.get_history(bot, 1)
        if snt.message_id == msg[0].message_id:
            nice = f"<b>☘️ @{bot} Status : ❌</b>\n\n"
        else:
            nice = f"<b>☘️ @{bot} Status : ✅</b>\n\n"
        first_msg = first_msg.replace(checking, nice)
        await reply.edit(first_msg, parse_mode="html")
        await userge.read_history(bot)
    tz = pytz.timezone("Asia/Kolkata")
    time_now = datetime.utcnow().astimezone(tz=tz).strftime("%I:%M %p - %d %B %Y")
    first_msg += f"<b>[Last Checked And Updated On : {time_now}]</b>"
    await reply.edit(first_msg, parse_mode="html")
