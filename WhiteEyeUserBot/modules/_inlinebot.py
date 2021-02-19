import os
import re
import urllib
from math import ceil
from re import findall
from urllib.parse import quote

import requests

# from pornhub_api import PornhubApi
from search_engine_parser import GoogleSearch
from telethon import Button, custom, events, functions
#from youtube_search import YoutubeSearch

from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP, CMD_LIST
from WhiteEyeUserBot import bot as client3
from WhiteEyeUserBot import client2 as client1
from WhiteEyeUserBot import client3 as client2
from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.functions import _deezer_dl, _ytdl, all_pro_s
from WhiteEyeUserBot.modules import inlinestats

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/e41d27e913a961d105d4d.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WhiteEye"

HELP_EMOJI = os.environ.get("HELP_EMOJI", None)
if not HELP_EMOJI:
    emji = "✘"
else:
    emji = HELP_EMOJI


@tgbot.on(events.InlineQuery)
async def inline_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id in o and query.startswith("WhiteEye"):
        rev_text = query[::-1]
        buttons = paginate_help(0, CMD_HELP, "helpme")
        result = builder.article(
            "© WhiteEyeUserBot Help",
            text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await event.answer([result])
    elif event.query.user_id in o and query == "stats":
        result = builder.article(
            title="Stats",
            text=f"**Showing Stats For {DEFAULTUSER}'s WhiteEye** \nNote --> Only Owner Can Check This \n(C) @WhiteEyeDevs",
            buttons=[
                [custom.Button.inline("Show Stats ?", data="terminator")],
                [
                    Button.url(
                        "Repo 🇮🇳", "https://github.com/WhiteEye-Org/WhiteEyeUserBot"
                    )
                ],
                [Button.url("Join Channel ❤️", "t.me/WhiteEyeDevs")],
            ],
        )
        await event.answer([result])
    elif event.query.user_id in o and query.startswith("**Hello"):
        result = builder.photo(
            file=WARN_PIC,
            text=query,
            buttons=[
                [
                    custom.Button.inline("❌ Spamming", data="dontspamnigga"),
                    custom.Button.inline("📝 Chatting", data="whattalk"),
                ],
                [
                    custom.Button.inline("❓ Doubt", data="askme"),
                    custom.Button.inline("🛑 Others", data="others"),
                ],
            ],
        )
        await event.answer([result] if result else None)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_popp_up_alert = "Please get your own WhiteEyeUserBot, and don't use mine!"
        await event.answer(reply_popp_up_alert, cache_time=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:  # pylint:disable=E0602
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1, CMD_HELP, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_pop_up_alert = "Please get your own WhiteEyeUserBot, and don't use mine!"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    )
)
async def on_plug_in_callback_query_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if not event.query.user_id in o:
        sedok = "Who The Fuck Are You? Get Your Own WhiteEye."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    plugin_name, page_number = event.data_match.group(1).decode("UTF-8").split("|", 1)
    if plugin_name in CMD_HELP:
        help_string = f"**💡 PLUGIN NAME 💡 :** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
    reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n\n**(C) @WhiteEyeDevs** ".format(plugin_name)
    if len(reply_pop_up_alert) >= 4096:
        crackexy = "`Pasting Your Help Menu.`"
        await event.answer(crackexy, cache_time=0, alert=True)
        out_file = reply_pop_up_alert
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        await event.edit(
            f"Pasted {plugin_name} to {url}",
            link_preview=False,
            buttons=[[custom.Button.inline("Go Back", data=f"backme_{page_number}")]],
        )
    else:
        await event.edit(
            message=reply_pop_up_alert,
            buttons=[[custom.Button.inline("Go Back", data=f"backme_{page_number}")]],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        text = inlinestats
        await event.answer(text, alert=True)
    else:
        txt = "You Can't View My Masters Stats"
        await event.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_dla_(.*)")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, bot)
    yt_dl_data = event.data_match.group(1).decode("UTF-8")
    link_s = yt_dl_data
    if event.query.user_id not in o:
        text = f"Please Get Your Own WhiteEye And Don't Waste My Resources"
        await event.answer(text, alert=True)
        return
    is_it = True
    await _ytdl(link_s, is_it, event, tgbot)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deezer_dl_(.*)")))
async def rip(event):
    sun = event.data_match.group(1).decode("UTF-8")
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        text = f"Please Get Your Own WhiteEye And Don't Waste My Resources"
        await event.answer(text, alert=True)
        return
    await _deezer_dl(sun, event, tgbot)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_vid_(.*)")))
async def rip(event):
    yt_dl_data = event.data_match.group(1).decode("UTF-8")
    o = await all_pro_s(Config, client1, client2, client3)
    link_s = yt_dl_data
    if event.query.user_id not in o:
        text = f"Please Get Your Own WhiteEye And Don't Waste My Resources"
        await event.answer(text, alert=True)
        return
    is_it = False
    await _ytdl(link_s, is_it, event, tgbot)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    text1 = "**You Have Chosed A Probhited Option. Therefore, You Have Been Blocked By WhiteEye. 💢.**"
    await event.edit(text1)
    await borg(functions.contacts.BlockRequest(event.query.user_id))
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Choose Probhited Option, So Has Been Blocked !** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(LOG_CHAT, message=PM_E)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backme_(.*)")))
async def sed(event):
    sedm = int(event.data_match.group(1).decode("UTF-8"))
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        sedok = "Who The Fuck Are You? Get Your Own Friday."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.answer("Back", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = paginate_help(sedm, CMD_HELP, "helpme")
    sed = f"""WhiteEyeUserBot Modules Are Listed Here !\n
For More Help or Support Visit @WhiteEyeDevs \nCurrently Loaded Plugins: {len(CMD_LIST)}"""
    await event.edit(message=sed, buttons=buttons)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit(
        "Ok. Please Wait Until My Master Approves. Don't Spam Or Try Anything Stupid. \nThank You For Contacting Me."
    )
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Wanted To Talk To You.** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(LOG_CHAT, message=PM_E)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Ok, Wait. You can Ask After Master Approves You. Kindly, Wait.")
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Wanted To Ask You Something** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(LOG_CHAT, message=PM_E)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"others")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Ok, Wait. You can Ask After Master Approves You. Kindly, Wait.")
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Wanted To Talk To You.** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(LOG_CHAT, message=PM_E)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cleuse")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        await event.edit("Help Menu Closed Successfully")
    if event.query.user_id not in o:
        sedok = "Who The Fuck Are You? Get Your Own WhiteEye."
        await event.answer(sedok, cache_time=0, alert=True)
        return


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 8
    number_of_cols = 2
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(emji, x, emji),
            data="us_plugin_{}|{}".format(x, page_number),
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⏪ Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("Close", data="cleuse"),
                custom.Button.inline(
                    "Next ⏩", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


@tgbot.on(events.InlineQuery(pattern=r"jm (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    o = await all_pro_s(Config, client1, client2, client3)
    builder = event.builder
    if event.query.user_id not in o:
        resultm = builder.article(
            title="Not Allowded",
            text=f"You Can't Use This Bot. \nDeploy WhiteEyeUserBot To Get Your Own Assistant, Deploy Link [Here](https://whiteeye-org.github.io/WhiteEyeUserBot/)",
        )
        await event.answer([resultm])
        return
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = f"http://starkmusic.herokuapp.com/result/?query={starkisnub}"
    seds = requests.get(url=search).json()
    for okz in seds:
        okz["album"]
        okmusic = okz["music"]
        hmmstar = okz["perma_url"]
        singer = okz["singers"]
        hmm = okz["duration"]
        langs = okz["language"]
        hidden_url = okz["media_url"]
        okayz = (
            f"**Song Name :** `{okmusic}` \n**Singer :** `{singer}` \n**Song Url :** `{hmmstar}`"
            f"\n**Language :** `{langs}` \n**Download Able Url :** `{hidden_url}`"
            f"\n**Duration :** `{hmm}`"
        )
        hmmkek = (
            f"Song : {okmusic} Singer : {singer} Duration : {hmm} \nLanguage : {langs}"
        )
        results.append(
            await event.builder.article(
                title=okmusic,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline(
                    "Search Again", query="jm ", same_peer=True
                ),
            )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"google (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy WhiteEyeUserBot To Get Your Own Assistant, Deploy Link [Here](https://whiteeye-org.github.io/WhiteEyeUserBot/)",
        )
        await event.answer([resultm])
        return
    results = []
    match = event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1

    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            okiknow = f"**GOOGLE - SEARCH** \n[{title}]({link})\n\n`{desc}`"
            results.append(
                await event.builder.article(
                    title=title,
                    description=desc,
                    text=okiknow,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="google ", same_peer=True
                        )
                    ],
                )
            )
        except IndexError:
            break
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"ph (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy WhiteEyeUserBot To Get Your Own Assistant, Deploy Link [Here](https://whiteeye-org.github.io/WhiteEyeUserBot/)",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(input_str, ordering="mostviewed")
    ok = 1
    for vid in data.videos:
        if ok <= 5:
            lul_m = f"**PORN-HUB SEARCH** \n**Video title :** `{vid.title}` \n**Video link :** `https://www.pornhub.com/view_video.php?viewkey={vid.video_id}`"
            results.append(
                await event.builder.article(
                    title=vid.title,
                    text=lul_m,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="ph ", same_peer=True
                        )
                    ],
                )
            )
        else:
            pass
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"xkcd (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy WhiteEyeUserBot To Get Your Own Assistant, Deploy Link [Here](https://whiteeye-org.github.io/WhiteEyeUserBot/)",
        )
        await event.answer([resultm])
        return
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url, params={"action": "xkcd", "query": quote(input_str)}
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        data.get("title")
        output_str = """
[XKCD]({})
Title: {}
Alt: {}
Day: {}
Month: {}
Year: {}""".format(
            xkcd_link, safe_title, alt, day, month, year
        )
        lul_k = builder.photo(file=img, text=output_str)
        await event.answer([lul_k])
    else:
        resultm = builder.article(title="- No Results :/ -", text=f"No Results Found !")
        await event.answer([resultm])


@tgbot.on(events.InlineQuery(pattern=r"deezer ?(.*)"))
async def inline_id_handler(event):
    builder = event.builder
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        resultm = builder.article(
            title="- Not Allowded -",
            text=f"You Can't Use This Bot. \nDeploy WhiteEyeUserBot To Get Your Own Assistant, Deploy Link [Here](https://whiteeye-org.github.io/WhiteEyeUserBot/)",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    link = f"https://api.deezer.com/search?q={input_str}&limit=7"
    dato = requests.get(url=link).json()
    # data_s = json.loads(data_s)
    for match in dato.get("data"):
        ro = str(match.get("id"))
        hmm_m = f"Title : {match['title']} \nLink : {match['link']} \nDuration : {match['duration']} seconds \nBy : {match['artist']['name']}"
        results.append(
            await event.builder.document(
                file=match["album"]["cover_big"],
                title=match["title"],
                text=hmm_m,
                description=f"Artist: {match['artist']['name']}\nAlbum: {match['album']['title']}",
                buttons=[
                    [
                        custom.Button.inline(
                            "Download Audio - mp3", data=f"deezer_dl_{ro}"
                        )
                    ],
                ],
            ),
        )
    if results:
        try:
            await event.answer(results)
        except TypeError:
            pass
