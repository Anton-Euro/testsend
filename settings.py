import sys
from typing import Optional

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

load_dotenv()


class Settings(BaseSettings):
    dp: Dispatcher = Field(default_factory=Dispatcher)
    tg_bot: Optional[Bot] = Field(default=None, init=False)
    user_ids: Optional[list[str]] = Field(default=None, init=False)

    FRONTEND_URL: str
    BOT_TOKEN: str = Field(default="")
    USER_IDS_PATH: str
    PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tg_bot = Bot(token=self.BOT_TOKEN)
        self.user_ids = Path(self.USER_IDS_PATH).read_text(encoding="utf-8").splitlines()


settings = Settings()