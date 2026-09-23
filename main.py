import logging

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
)

from config import BOT_TOKEN

from bot.handlers.start import start_command
from bot.handlers.user import help_command, about_command, status_command
from bot.handlers.admin import admin_command
from bot.handlers.features import (
    ai_command,
    agent_command,
    creative_command,
    research_command,
    community_command,
    business_command,
    settings_command,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def handle_callback(update, context):
    query = update.callback_query
    await query.answer()

    callback_data = query.data or "about"
    text_map = {
        "ai_tools": "🧠 <b>AI Tools</b>\n\nThe bot can guide you through AI workflows, content ideas, research prompts, and smart task planning.",
        "agents": "🤖 <b>Agents</b>\n\nThe system is organized around a multi-agent design with planning, execution, tools, and scheduling building blocks.",
        "creative": "🎨 <b>Creative</b>\n\nGenerate campaign ideas, prompts, captions, scripts, and audio/video concepts in a single workspace.",
        "research": "🔬 <b>Research</b>\n\nUse research lab flows to define questions, plan steps, and summarize sources and findings.",
        "community": "👥 <b>Community</b>\n\nThis module helps with onboarding, rules, announcements, and community management features.",
        "business": "💼 <b>Business</b>\n\nCreate customer records, tasks, and reporting workflows using the business toolkit.",
        "settings": "⚙️ <b>Settings</b>\n\nBot settings can be expanded with owner-level configuration, moderation controls, and automation preferences.",
        "about": "👑 <b>MYSTERIOUS GLOQBOT</b>\n\nA Telegram power bot in 2026, built for AI, automation, community management, and operational workflows.",
    }

    await query.edit_message_text(
        text_map.get(callback_data, text_map["about"]),
        parse_mode="HTML",
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing. Add it to your .env file.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("admin", admin_command))
    app.add_handler(CommandHandler("ai", ai_command))
    app.add_handler(CommandHandler("agents", agent_command))
    app.add_handler(CommandHandler("creative", creative_command))
    app.add_handler(CommandHandler("research", research_command))
    app.add_handler(CommandHandler("community", community_command))
    app.add_handler(CommandHandler("business", business_command))
    app.add_handler(CommandHandler("settings", settings_command))
    app.add_handler(CallbackQueryHandler(handle_callback))

    logger.info("👑 MYSTERIOUS GLOQBOT is starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
