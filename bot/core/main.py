"""This module contains the main entry point for the proxy seller bot."""

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.cache.redis import storage
from bot.core.config import settings
from bot.handlers import main_router
from bot.middlewares.i18n import i18n_middleware


async def main() -> None:
    """Create the entry instances and start the bot.

    Args: None

    Returns: None

    Raises: None
    """
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher(storage=storage)

    dp.update.middleware.register(i18n_middleware)

    dp.include_router(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    """Run the bot."""
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
