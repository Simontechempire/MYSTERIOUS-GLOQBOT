import os

from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN", "")

BOT_NAME = os.getenv(
    "BOT_NAME",
    "MYSTERIOUS GLOQBOT"
)

BOT_VERSION = os.getenv(
    "BOT_VERSION",
    "1.0.0"
)

OWNER_ID = os.getenv(
    "OWNER_ID",
    ""
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)
