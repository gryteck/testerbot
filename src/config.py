from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

media_groups = []


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']

    SUPPORT_ID: int

    PROMO_URL: str

    TOKEN: str

    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASS: str
    PG_NAME: str

    RD_HOST: str
    RD_PASS: str

    @property
    def PG_URL(self):
        return f"postgresql+asyncpg://" \
               f"{self.PG_USER}:" \
               f"{self.PG_PASS}@" \
               f"{self.PG_HOST}:" \
               f"{self.PG_PORT}/" \
               f"{self.PG_NAME}"

    @property
    def RD_URL(self):
        return f"redis://{self.RD_PASS}@{self.RD_HOST}:6379/1"

    TEST_TOKEN: str

    TEST_PG_HOST: str
    TEST_PG_PORT: int
    TEST_PG_USER: str
    TEST_PG_PASS: str
    TEST_PG_NAME: str

    TEST_RD_HOST: str
    TEST_RD_PASS: str

    @property
    def TEST_PG_URL(self):
        return f"postgresql+asyncpg://" \
               f"{self.TEST_PG_USER}:" \
               f"{self.TEST_PG_PASS}@" \
               f"{self.TEST_PG_HOST}:" \
               f"{self.TEST_PG_PORT}/" \
               f"{self.TEST_PG_NAME}"

    @property
    def TEST_RD_URL(self):
        return f"redis://{self.TEST_RD_PASS}@{self.TEST_RD_HOST}:6379/1"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')


settings = Settings()

if settings.MODE == 'TEST':
    bot = Bot(token=settings.TEST_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
else:
    bot = Bot(token=settings.TOKEN)
