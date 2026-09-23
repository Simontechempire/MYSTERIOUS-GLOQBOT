from telegram import Update
from telegram.ext import ContextTypes


async def channel_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.effective_chat:
        return

    chat = update.effective_chat

    await update.message.reply_text(
        "📢 <b>GLOQ CHANNEL</b>\n\n"
        f"📌 Name: {chat.title or 'Channel'}\n"
        f"🆔 ID: <code>{chat.id}</code>\n"
        f"💬 Type: {chat.type}",
        parse_mode="HTML"
    )
