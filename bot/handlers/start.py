"""Start handler module.

This module contains the start handler for the bot.
"""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    """Start handler for the bot.

    Parameters:
        message (Message): The message object.

    Returns:
        None
    """
    start_text = _("start text")

    await message.answer(start_text)
