import os
from pydantic import BaseSettings
from dotenv import load_dotenv
from sqlalchemy import URL

# Determine the environment
ENV = os.getenv('ENV', 'local')

# Load the appropriate .env file
if ENV == 'production':
    dotenv_path = '.env.production'
elif ENV == 'staging':
    dotenv_path = '.env.staging'
else:
    dotenv_path = '.env'

load_dotenv(dotenv_path)

class Settings(BaseSettings):
    # Database configuration
    # For more information on pool configuration, read:
    # https://docs.sqlalchemy.org/en/20/core/pooling.html
    db_max_pool_size: int = 5
    db_overflow_size: int = 10
    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str

    class Config:
        env_file = dotenv_path
        env_file_encoding = 'utf-8'


    @property
    def db_postgres(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )