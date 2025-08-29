from motor.motor_asyncio import AsyncIOMotorClient
import os
from EsproMusic import LOGGER  # Make sure LOGGER is initialized

LOGGER(__name__).info("Connecting to your Mongo Database...")

MONGO_URL = os.environ.get("MONGO_URL")
if not MONGO_URL:
    LOGGER(__name__).error("MONGO_URL environment variable not set! Exiting...")
    raise ValueError("MONGO_URL is required")

try:
    # Async Mongo client
    mongo_client = AsyncIOMotorClient(MONGO_URL)
    # Central database for your bot
    db = mongo_client["EsproMusicDB"]

    # Collections
    waifu_collection = db["waifus"]
    music_collection = db["music"]
    users_collection = db["users"]
    banned_collection = db["banned_users"]
    gbanned_collection = db["gbanned_users"]

    LOGGER(__name__).info("Connected to Mongo Database successfully.")
except Exception as e:
    LOGGER(__name__).error(f"Failed to connect to Mongo Database: {e}")
    exit()
