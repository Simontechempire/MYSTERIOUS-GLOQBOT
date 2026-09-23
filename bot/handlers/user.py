from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = """
👑 <b>MYSTERIOUS GLOQBOT</b>

<b>Commands</b>

/start — Open main menu
/help — Show help
/about — About the bot

More AI features are coming soon.
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )
