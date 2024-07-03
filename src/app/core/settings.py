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
    
    # Find and load the .env file
    #load_dotenv(find_dotenv(filename=".env", usecwd=True))
    DOTENV = os.path.join(os.path.dirname(__file__), ".env")
    breakpoint()
    model_config = SettingsConfigDict(
        env_file=find_dotenv(filename=DOTENV), env_file_encoding="utf-8", extra="ignore"
    )
    breakpoint()
    @property
    def db_postgres(self) -> URL:
        breakpoint()
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
    def db_data_source_name(self) -> str:
        return f"postgresql://{self.db_user}:{self._db_password_escaped_for_alembic}@{self.db_host}/{self.db_name}"
    
#@lru_cache
def get_settings() -> Settings:
    return Settings()
    