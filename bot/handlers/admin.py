from config import OWNER_ID


async def admin_command(update, context):
    user_id = str(update.effective_user.id)

    if user_id != str(OWNER_ID):
        await update.message.reply_text("🚫 You aren't the owner of this bot.")
        return

    await update.message.reply_text(
        "👑 <b>OWNER PANEL</b>\n\n"
        "✅ Access granted.\n"
        "🛠️ Bot tools are active.\n"
        "📊 System status: stable.",
        parse_mode="HTML",
    )
