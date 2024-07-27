import urllib
from functools import lru_cache

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL
import os

class Settings(BaseSettings):
    # Database configuration
    # For more information on pool configuration, read:
    # https://docs.sqlalchemy.org/en/20/core/pooling.html
    
    db_max_pool_size: int = 10
    db_overflow_size: int = 10
    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    
    # Application configuration
    app_env: str  # dev, test, ci, prod
    
    # docker compose exec -it web  poetry run alembic upgrade head
    model_config = SettingsConfigDict(
        env_prefix="APP_", env_file=find_dotenv(".env"), env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def db(self) -> URL:
        print(self.db_user)
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )

    @property
    def _db_password_escaped_for_alembic(self) -> str:
        """Return the password escaping the special characters as required for Alembic.
        Follows recomendation on https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls.
        """
        return urllib.parse.quote_plus(self.db_password).replace("%", "%%")

    @property
    def db_connection_string(self) -> str:
        return f"postgresql://{self.db_user}:{self._db_password_escaped_for_alembic}@{self.db_host}/{self.db_name}"
    
@lru_cache
def get_settings() -> Settings:
    return Settings()
    