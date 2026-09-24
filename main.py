import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from bot.handlers import setup_routers
from bot.middlewares.force_join import ForceJoinMiddleware

try:
    import uvloop
    uvloop.install()
except ImportError:
    pass


async def main() -> None:
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        stream=sys.stdout,
    )

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.message.middleware(ForceJoinMiddleware())
    dp.callback_query.middleware(ForceJoinMiddleware())

    root_router = setup_routers()
    dp.include_router(root_router)

    me = await bot.get_me()
    logging.info(f"Starting {me.full_name} (@{me.username})")
    logging.info(f"Owner: {settings.OWNER_NAME} (@{settings.OWNER_USERNAME}) | ID: {settings.OWNER_ID}")
    logging.info(f"Force Join: {settings.force_join_chats}")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
