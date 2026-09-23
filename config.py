from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Bot
    BOT_TOKEN: str

    # Owner
    OWNER_ID: int
    OWNER_USERNAME: str = "Queen_Tech_00"
    OWNER_NAME: str = "Queen tech"

    # Force Join (usernames without @)
    FORCE_JOIN_CHANNEL: str = "queentechchannel"
    FORCE_JOIN_GROUP: str = "queentechgroup"
    FORCE_JOIN_SIMON: str = "babyupdategc"

    # Extra admins (comma separated in env)
    ADMIN_IDS: str = ""

    # Optional
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/bot.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    LOG_LEVEL: str = "INFO"

    @property
    def admin_ids(self) -> List[int]:
        ids = []
        if self.OWNER_ID:
            ids.append(self.OWNER_ID)
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
