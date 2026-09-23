from telegram import Update
from telegram.ext import ContextTypes

from bot.utils.texts import (
    AI_TEXT,
    AGENT_TEXT,
    CREATIVE_TEXT,
    RESEARCH_TEXT,
    COMMUNITY_TEXT,
    BUSINESS_TEXT,
    SETTINGS_TEXT,
)


async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AI_TEXT, parse_mode="HTML")


async def agent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AGENT_TEXT, parse_mode="HTML")


async def creative_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CREATIVE_TEXT, parse_mode="HTML")


async def research_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RESEARCH_TEXT, parse_mode="HTML")


async def community_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(COMMUNITY_TEXT, parse_mode="HTML")


async def business_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BUSINESS_TEXT, parse_mode="HTML")


async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SETTINGS_TEXT, parse_mode="HTML")
