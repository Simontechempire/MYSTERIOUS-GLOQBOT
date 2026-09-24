import asyncio
import logging

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
)

from config import BOT_TOKEN, LOG_LEVEL

from bot.handlers.admin import admin_command

from bot.handlers.features import (
    agent_command,
    ai_command,
    business_command,
    community_command,
    creative_command,
    research_command,
    settings_command,
)

from bot.handlers.start import start_command

from bot.handlers.user import (
    about_command,
    help_command,
    status_command,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=getattr(
        logging,
        LOG_LEVEL.upper(),
        logging.INFO,
    ),
)

logger = logging.getLogger(__name__)


CALLBACK_TEXT = {
    "ai_tools": (
        "🧠 <b>AI Tools</b>\n\n"
        "AI workflows, content ideas, research prompts, "
        "and smart task planning."
    ),

    "agents": (
        "🤖 <b>Agents</b>\n\n"
        "Planner, executor, scheduler, and reusable "
        "tool registry components."
    ),

    "creative": (
        "🎨 <b>Creative</b>\n\n"
        "Creative prompts, captions, scripts, "
        "and multimedia concepts."
    ),

    "research": (
        "🔬 <b>Research</b>\n\n"
        "Research questions, structured plans, "
        "analysis, and summaries."
    ),

    "community": (
        "👥 <b>Community</b>\n\n"
        "Welcome messages, announcements, rules, "
        "and moderation support."
    ),

    "business": (
        "💼 <b>Business</b>\n\n"
        "Customer records, tasks, reports, "
        "and operational workflows."
    ),

    "settings": (
        "⚙️ <b>Settings</b>\n\n"
        "Owner configuration, moderation controls, "
        "and automation preferences."
    ),

    "about": (
        "👑 <b>MYSTERIOUS GLOQBOT</b>\n\n"
        "A Telegram power bot built for AI, "
        "automation, communities, and business workflows."
    ),
}


async def handle_callback(update, context):
    query = update.callback_query

    if query is None:
        return

    await query.answer()

    await query.edit_message_text(
        CALLBACK_TEXT.get(
            query.data,
            CALLBACK_TEXT["about"],
        ),
        parse_mode="HTML",
    )


def build_application() -> Application:

    if not BOT_TOKEN or BOT_TOKEN.startswith("YOUR_"):
        raise RuntimeError(
            "BOT_TOKEN is missing or still a placeholder. "
            "Set BOT_TOKEN in Render environment variables."
        )

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    commands = {
        "start": start_command,
        "help": help_command,
        "about": about_command,
        "status": status_command,
        "admin": admin_command,
        "ai": ai_command,
        "agents": agent_command,
        "creative": creative_command,
        "research": research_command,
        "community": community_command,
        "business": business_command,
        "settings": settings_command,
    }

    for name, callback in commands.items():
        app.add_handler(
            CommandHandler(
                name,
                callback,
            )
        )

    app.add_handler(
        CallbackQueryHandler(
            handle_callback
        )
    )

    return app


async def main():

    logger.info(
        "👑 MYSTERIOUS GLOQBOT is starting..."
    )

    app = build_application()

    await app.initialize()

    await app.start()

    if app.updater is None:
        raise RuntimeError(
            "Telegram updater is not available."
        )

    await app.updater.start_polling(
        drop_pending_updates=True
    )

    logger.info(
        "✅ MYSTERIOUS GLOQBOT is online."
    )

    try:
        await asyncio.Event().wait()

    except (KeyboardInterrupt, SystemExit):
        logger.info(
            "🛑 MYSTERIOUS GLOQBOT is shutting down..."
        )

    finally:

        if app.updater.running:
            await app.updater.stop()

        await app.stop()

        await app.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
