from telegram import Update
from telegram.ext import ContextTypes

from bot.filters.is_admin import is_admin
from bot.utils.moderation import (
    restricted_permissions,
    normal_permissions,
)


async def group_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.effective_chat:
        return

    chat = update.effective_chat

    await update.message.reply_text(
        "👥 <b>GLOQ GROUP</b>\n\n"
        f"📌 Name: {chat.title or 'Private Chat'}\n"
        f"🆔 ID: <code>{chat.id}</code>\n"
        f"💬 Type: {chat.type}",
        parse_mode="HTML"
    )


async def mute_user(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not await is_admin(update):
        await update.message.reply_text(
            "🚫 Only group administrators can use this command."
        )
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "↩️ Reply to a user's message with /mute."
        )
        return

    target = update.message.reply_to_message.from_user

    try:
        await update.effective_chat.restrict_member(
            target.id,
            permissions=restricted_permissions()
        )

        await update.message.reply_text(
            f"🔇 <b>{target.first_name}</b> has been muted.",
            parse_mode="HTML"
        )

    except Exception as error:
        await update.message.reply_text(
            f"❌ Could not mute user.\n\n{error}"
        )


async def unmute_user(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not await is_admin(update):
        await update.message.reply_text(
            "🚫 Only group administrators can use this command."
        )
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "↩️ Reply to a user's message with /unmute."
        )
        return

    target = update.message.reply_to_message.from_user

    try:
        await update.effective_chat.restrict_member(
            target.id,
            permissions=normal_permissions()
        )

        await update.message.reply_text(
            f"🔊 <b>{target.first_name}</b> has been unmuted.",
            parse_mode="HTML"
        )

    except Exception as error:
        await update.message.reply_text(
            f"❌ Could not unmute user.\n\n{error}"
        )
