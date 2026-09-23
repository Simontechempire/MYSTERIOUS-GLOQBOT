import logging

from telegram.ext import (
    Application,
    CommandHandler,
)

from config import BOT_TOKEN

from bot.handlers.start import start_command
from bot.handlers.user import help_command
from bot.handlers.admin import admin_command


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing. Add it to your .env file."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start_command)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        CommandHandler("admin", admin_command)
    )

    logger.info(
        "👑 MYSTERIOUS GLOQBOT is starting..."
    )

    app.run_polling()


if __name__ == "__main__":
    main()
