#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import os

import wget
from youtubesearchpython import SearchVideos

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.utils import WhiteEye_on_cmd, edit_or_reply, sudo_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern="ytmusic ?(.*)"))
@WhiteEye.on(sudo_cmd(pattern="ytmusic ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    whiteeyez = mio[0]["id"]
    mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{whiteeyez}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Config.TMP_DOWNLOAD_DIRECTORY
    sedlyf = wget.download(kekme, out=path)
    stark = (
        f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k '
        + mo
    )
    os.system(stark)
    await asyncio.sleep(4)
    km = f"./music/{thum}.mp3"
    if os.path.exists(km):
        await myself_stark.edit("`Song Downloaded Sucessfully. Let Me Upload it Here.`")
    else:
        await myself_stark.edit("`SomeThing Went Wrong. Try Again After Sometime..`")
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await borg.send_file(
        event.chat_id,
        km,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        performer=thums,
        supports_streaming=True,
    )
    await myself_stark.edit("`Song Uploaded. By (C) @WhiteEyeDevs`")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "ytmusic": "**Ytmusic**\
\n\n**Syntax : **`.ytmusic <song name>`\
\n**Usage :** Downloads songs from ytmusic"
    }
)