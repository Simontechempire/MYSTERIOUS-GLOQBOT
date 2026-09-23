import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"👑 Welcome to MYSTERIOUS GLOQBOT, {user.first_name}!\n\n"
        "🤖 Your multi-agent AI operating system is online.\n\n"
        "Use /help to explore the available features."
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "👑 MYSTERIOUS GLOQBOT\n\n"
        "Available commands:\n\n"
        "/start — Start the bot\n"
        "/help — Show help\n"
        "/about — About GLOQBOT"
    )


async def about(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "👑 MYSTERIOUS GLOQBOT\n\n"
        "⚡ Full Multi-Agent AI Operating System\n"
        "🧠 AI Intelligence Layer\n"
        "🤖 Agent Engine\n"
        "📱 Telegram Native\n"
        "🔐 Privacy & Security\n\n"
        "Version: 1.0.0"
    )


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing. Add it to your .env file."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    logger.info("MYSTERIOUS GLOQBOT is starting...")

    app.run_polling()


if __name__ == "__main__":
    main()
