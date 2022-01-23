
import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from ShuKurenaiXRoBot import (StartTime, DEV_USERS, pgram)
import ShuKurenaiXRoBot.utils.formatter as formatter
import ShuKurenaiXRoBot.modules.sql.users_sql as sql




# Stats Module

async def bot_sys_stats():
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    users = sql.num_users()
    chats = sql.num_chats()
    stats = f"""
âž¢ ShuKurenai's Current System Stats

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
â€¢ UPTIME: {formatter.get_readable_time((bot_uptime))}
â€¢ BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
â€¢ CPU: {cpu}%
â€¢ RAM: {mem}%
â€¢ DISK: {disk}%
â€¢ CHATS: {chats}
â€¢ USERS: {users}
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
"""
    return stats
