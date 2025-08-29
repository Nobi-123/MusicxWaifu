# EsproMusic package init - cleaned
import os
from pyrogram import Client, filters as f
from pyrogram.types import *

# Global state dicts (kept as in original)
locks = {}
message_counters = {}
spam_counters = {}
last_characters = {}
sent_characters = {}
first_correct_guesses = {}
message_counts = {}
last_user = {}
warned_users = {}
user_cooldowns = {}
user_nguess_progress = {}
user_guess_progress = {}
normal_message_counts = {}

# Unit imports (keep existing unit modules)
from EsproMusic.unit.ban import *
from EsproMusic.unit.sudo import *
from EsproMusic.unit.react import *
from EsproMusic.unit.send_img import *
from EsproMusic.unit.rarity import *

# Core setup
from EsproMusic.core.bot import Loy
from EsproMusic.core.dir import dirr
from EsproMusic.core.git import git
from EsproMusic.core.userbot import Userbot

dirr()
git()

app = Loy()
userbot = Userbot()

# Export LOGGER if available from logging module
try:
    from EsproMusic.logging import LOGGER
except Exception:
    LOGGER = None

__all__ = ['app', 'userbot', 'locks', 'LOGGER']
