"""Redis cache for bot"""

from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import ConnectionPool, Redis

from bot.core.config import settings

redis_client = Redis(
    connection_pool=ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASS,
        db=0,
    ),
)

storage = RedisStorage(
    redis=redis_client,
    key_builder=DefaultKeyBuilder(with_bot_id=True),
)
