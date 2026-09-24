from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

from config import OWNER_ID


class IsOwner(BaseFilter):
    async def __call__(self, event: TelegramObject) -> bool:
        user = getattr(event, "from_user", None)

        if not user:
            return False

        return user.id == OWNER_ID
