"""i18n middleware.

Bot middleware for handling internationalization in the bot.
"""

from aiogram.utils.i18n import FSMI18nMiddleware, I18n

i18n = I18n(path="bot/locales", default_locale="en")

i18n_middleware = FSMI18nMiddleware(i18n)
