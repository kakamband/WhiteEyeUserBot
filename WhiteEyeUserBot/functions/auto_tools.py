import asyncio
import time
import random
from telethon.tl import functions
from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot import bot
import pytz
import asyncio
import os
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import os
import logging
from datetime import datetime
m = logging.getLogger("AUTOTOOLS")

bio_temp = ["Making History.", "I'm on energy-saving mode.", "Success is in my blood.", "Life F$@ks me, now it's my turn.", "Error 404: Bio unavailable."]

async def auto_name(name=None):
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    nameof = name if name else Config.ALIVE_NAME
    oof = datetime_tz.strftime(f"🕒 %d/%m/%Y ⚡{nameof}⚡ 📅 %H:%M")
    try:
        await bot(
                functions.account.UpdateProfileRequest(
                    first_name=oof
                )
            )
    except Exception as e:
        m.warning(f"Failed AutoName Due To : {e}")
    return    
    
async def auto_bio(bio=None):
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    bioof = bio if bio else random.choice(bio_temp)
    oof = datetime_tz.strftime(f'🕒%d/%m/%Y "{bioof}" 📅%H:%M')
    try:
        await bot(
                functions.account.UpdateProfileRequest(
                    about=oof
                )
            )
    except Exception as e:
        m.warning(f"Failed AutoBio Due To : {e}")
    return    

counter = -30

async def auto_pic():
    global counter
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    downloaded_file_name = "WhiteEyeUserBot/original_pic.png"
    if not os.path.exists(downloaded_file_name):
        downloader = SmartDL(
        Config.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False
            )
        downloader.start(blocking=False)
        photo = "fridaybot/photo_pfp.png"
        while not downloader.isFinished():
            pass
    else:
        pass
    img = Image.open(downloaded_file_name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/Streamster.ttf', 220)
    file_test = img.rotate(counter, expand=False)
    image_widthz, image_heightz = img.size
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    text = datetime_tz.strftime('%H:%M')
    w,h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    file_name = "autopic_friday.png"
    img.save(file_name, "PNG")
    file = await bot.upload_file(file_name)
    try:
            await bot(
                functions.photos.UploadProfilePhotoRequest(file)
            )
            os.remove(file_name)
            counter -= 30
    except:
            return
    return
