import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from EsproMusic.core.client import app, userbot              # Fixed import for clients
from EsproMusic.utils.logging import LOGGER                 # Fixed import for LOGGER
from EsproMusic.core.call import Loy
from EsproMusic.misc import sudo
from EsproMusic.plugins import ALL_MODULES
from EsproMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # Check if assistant client variables are defined
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "Assistant client variables not defined, exiting..."
        )
        exit()

    # Run sudo initialization
    await sudo()

    # Load banned users from database
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    # Start main bot
    await app.start()

    # Dynamically import all plugin modules
    for all_module in ALL_MODULES:
        importlib.import_module("EsproMusic.plugins" + all_module)
    LOGGER("EsproMusic.plugins").info("Successfully Imported Modules...")

    # Start userbot (string-session)
    await userbot.start()

    # Start PyTgCalls
    await Loy.start()

    # Attempt to stream default media in VC
    try:
        await Loy.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("EsproMusic").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except Exception:
        pass

    # Initialize PyTgCalls decorators
    await Loy.decorators()

    LOGGER("EsproMusic").info(
        "EsproMusicBot Started Successfully \n\n"
        "Yaha App ko nahi aana hai aapni hf jo bhej sakte hai @Esprosupport"
    )

    # Keep bot and userbot running
    await idle()

    # Stop both clients gracefully
    await app.stop()
    await userbot.stop()
    LOGGER("EsproMusic").info("Stopping Espro Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
