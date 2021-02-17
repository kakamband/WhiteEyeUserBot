from WhiteEyeUserBot.Configs import Config
from googletrans import LANGUAGES
from google_trans_new import google_translator


async def tr(event, text):
    we = Config.LANG if LANGUAGES.get(Config.LANG) else 'en'
    if we == 'en':
        await event.edit(text)
    else:
        translator = google_translator()
        translated = translator.translate(text ,lang_tgt=we)
        await event.edit(translated)
    return
