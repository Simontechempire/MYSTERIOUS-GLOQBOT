from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    BOT_TOKEN: str

    OWNER_ID: int
    OWNER_USERNAME: str = "Queen_Tech_00"
    OWNER_NAME: str = "Queen tech"

    FORCE_JOIN_CHANNEL: str = "queentechchannel"
    FORCE_JOIN_GROUP: str = "queentechgroup"
    FORCE_JOIN_SIMON: str = "babyupdategc"

    ADMIN_IDS: str = ""

    DATABASE_URL: str = "sqlite+aiosqlite:///./data/bot.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    LOG_LEVEL: str = "INFO"

    @property
    def admin_ids(self) -> List[int]:
        ids = [self.OWNER_ID]
        if self.ADMIN_IDS:
            for part in self.ADMIN_IDS.split(","):
                part = part.strip()
                if part.isdigit():
                    ids.append(int(part))
        return list(set(ids))

    @property
    def force_join_chats(self) -> List[str]:
        return [
            self.FORCE_JOIN_CHANNEL,
            self.FORCE_JOIN_GROUP,
            self.FORCE_JOIN_SIMON,
        ]


settings = Settings()
