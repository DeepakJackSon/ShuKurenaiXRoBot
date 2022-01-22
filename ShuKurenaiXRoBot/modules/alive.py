import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from ShuKurenaiXRoBot.events import register
from ShuKurenaiXRoBot import telethn as borg, OWNER_ID
from ShuKurenaiXRoBot import StartTime, dispatcher
from ShuKurenaiXRoBot import SUPPORT_CHAT
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/3cd1f5776c3ea08f609f4.jpg"
file2 = "https://telegra.ph/file/e384ab52db8c0912ca356.jpg"
file3 = "https://telegra.ph/file/0adf9e97735ba8a420973.jpg"
file4 = "https://telegra.ph/file/2861eda5afba02bf04254.jpg" 
file5 = "https://telegra.ph//file/f218b08b076fa31df028b.jpg"
file6 = "https://telegra.ph//file/75280e721b12b8b4a18a4.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Shu = f"♡ **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm ShuKurenai**\n\n"
    Shu += f"♡ **My Uptime** ~♪ `{uptime}`\n\n"
    Shu += f"♡ **Telethon Version** ~♪ `{version.__version__}`\n\n"
    Shu += f"♡ **Python Telegram Bot Version** ~♪ `{telegram.__version__}`\n\n"
    Shu += f"♡ **Pyrogram Version** ~♪ `{pyro}`\n\n"
    Shu += f"♡ **My Master** ~♪ [DeepakJack](tg://user?id={OWNER_ID})"
    BUTTON = [[Button.url("Support Chat", f"https://t.me/{SUPPORT_CHAT}"), Button.url("Updates Channel", "https://t.me/shukurenai007")]]
    on = await borg.send_file(yes.chat_id, file=file2,caption=Shu, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file3, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file6, buttons=BUTTON)
