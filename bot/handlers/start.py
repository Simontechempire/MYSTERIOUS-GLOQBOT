from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.main_menu import main_menu
from bot.utils.texts import WELCOME_TEXT


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="HTML",
        reply_markup=main_menu()
    )
