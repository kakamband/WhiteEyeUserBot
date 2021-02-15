# All 3 Clients
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession

from WhiteEyeUserBot.Configs import Config

hudson = logging.getLogger("ALERT")


if not Config.STRING_SESSION:
    hudson.warning(
        "String Session is Missing, WhiteEyeUserBot is Quiting. Please Check ReadMe"
    )
    quit(1)

if not Config.APP_ID:
    hudson.warning("Api ID is Missing, WhiteEyeUserBot is Quiting. Please Check ReadMe")
    quit(1)

if not Config.API_HASH:
    hudson.warning(
        "Api Hash is Missing, WhiteEyeUserBot is Quiting. Please Check ReadMe"
    )
    quit(1)

if not Config.PRIVATE_GROUP_ID:
    hudson.warning(
        "Please Add Private Group ID For Proper Functioning Of WhiteEyeUserBot"
    )
    quit(1)

if Config.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Config.APP_ID, Config.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)
if Config.STRING_SESSION_2:
    client2 = TelegramClient(
        StringSession(Config.STRING_SESSION_2), Config.APP_ID, Config.API_HASH
    )
else:
    client2 = None
if Config.STRING_SESSION_3:
    client3 = TelegramClient(
        StringSession(Config.STRING_SESSION_3), Config.APP_ID, Config.API_HASH
    )
else:
    client3 = None
