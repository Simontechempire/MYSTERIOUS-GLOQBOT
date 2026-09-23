import logging
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
BOT_NAME = os.getenv("BOT_NAME", "MYSTERIOUS GLOQBOT").strip()
BOT_VERSION = os.getenv("BOT_VERSION", "1.0.0").strip()
OWNER_ID = os.getenv("OWNER_ID", "").strip()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").strip().upper()

if LOG_LEVEL not in logging._nameToLevel:
    LOG_LEVEL = "INFO"
