from pyrogram import Client
import os

# ---------------------------
# Bot account
# ---------------------------
app = Client(
    "EsproMusicBot",
    bot_token=os.environ.get("TOKEN"),
    api_id=int(os.environ.get("API_ID", 0)),
    api_hash=os.environ.get("API_HASH", "")
)

# ---------------------------
# Userbot account (String Session)
# ---------------------------
userbot = Client(
    "EsproMusicUser",
    session_string=os.environ.get("STRING_SESSION"),
    api_id=int(os.environ.get("API_ID", 0)),
    api_hash=os.environ.get("API_HASH", "")
)
