from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, CallbackQuery, TelegramObject, ChatMember
from aiogram.enums import ChatMemberStatus
from config import settings
from bot.keyboards.stylish import force_join_keyboard
from bot.utils.texts import FORCE_JOIN_TEXT, NOT_MEMBER_TEXT


ALLOWED_CALLBACKS = {"check_force_join"}


class ForceJoinMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        bot: Bot = data["bot"]
        user = None

        if isinstance(event, Message):
            user = event.from_user
        elif isinstance(event, CallbackQuery):
            user = event.from_user
            if event.data in ALLOWED_CALLBACKS:
                return await handler(event, data)

        if user is None:
            return await handler(event, data)

        if user.id in settings.admin_ids:
            return await handler(event, data)

        is_member = await self._check_all_memberships(bot, user.id)
        if is_member:
            return await handler(event, data)

        if isinstance(event, Message):
            await event.answer(FORCE_JOIN_TEXT, reply_markup=force_join_keyboard(), parse_mode="HTML")
            return None

        if isinstance(event, CallbackQuery):
            await event.answer(NOT_MEMBER_TEXT, show_alert=True)
            try:
                await event.message.edit_text(FORCE_JOIN_TEXT, reply_markup=force_join_keyboard(), parse_mode="HTML")
            except Exception:
                await event.message.answer(FORCE_JOIN_TEXT, reply_markup=force_join_keyboard(), parse_mode="HTML")
            return None

        return None

    async def _check_all_memberships(self, bot: Bot, user_id: int) -> bool:
        allowed = {
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.CREATOR,
            ChatMemberStatus.RESTRICTED,
        }
        for chat in settings.force_join_chats:
            try:
                member: ChatMember = await bot.get_chat_member(chat_id=f"@{chat}", user_id=user_id)
                if member.status not in allowed:
                    return False
            except Exception:
                return False
        return True
