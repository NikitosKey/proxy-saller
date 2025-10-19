"""Bot handlers.

This package contains various handlers for the bot.
"""

from aiogram import Router

from bot.handlers.start import start_router

main_router = Router()

main_router.include_router(start_router)


__init__ = ["main_router"]
