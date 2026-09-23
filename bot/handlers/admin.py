from telegram import Update
from telegram.ext import ContextTypes

from config import OWNER_ID


async def admin_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    user_id = str(update.effective_user.id)

    if user_id != str(OWNER_ID):
        await update.message.reply_text(
            "🚫 You you you aren't my owner ."
        )
        return

    await update.message.reply_text(
        "👑 <b>OWNER PANEL</b>\n\n"
        "✅ Access granted.",
        parse_mode="HTML"
    )
