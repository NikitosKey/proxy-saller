"""This module loads a settings from .env_file."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine.url import URL


class EnvBaseSettings(BaseSettings):
    """Base settings class to load environment variables from a .env file."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False
    )


class BotSettings(EnvBaseSettings):
    """Bot settings class to load bot-specific environment variables."""

    BOT_TOKEN: str = ""


class DBSettings(EnvBaseSettings):
    """Database settings class to load database-specific environment variables."""

    DB_HOST: str = "postgres"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str | None = None
    DB_NAME: str = "postgres"

    @property
    def database_url(self) -> URL | str:
        """Construct the database URL for SQLModel.

        Returns:
            URL | str: The constructed database URL.

        Example:
            postgresql+asyncpg://user:password@host:port/dbname

        """
        if self.DB_PASS:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class CacheSettings(EnvBaseSettings):
    """Cache settings class to load cache-specific environment variables."""

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASS: str | None = None


class Settings(BotSettings, DBSettings, CacheSettings):
    """Settings class to load all environment variables."""

    DEBUG: bool = True


settings = Settings()
