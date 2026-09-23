from telegram import Update
from telegram.ext import ContextTypes

from bot.utils.texts import ABOUT_TEXT, HELP_TEXT, STATUS_TEXT


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(HELP_TEXT, parse_mode="HTML")


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(ABOUT_TEXT, parse_mode="HTML")


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(STATUS_TEXT, parse_mode="HTML")
