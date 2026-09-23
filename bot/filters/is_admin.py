from telegram import Update
from telegram.constants import ChatMemberStatus


async def is_admin(
    update: Update,
    user_id: int | None = None
) -> bool:

    if not update.effective_chat:
        return False

    if not user_id:
        user_id = update.effective_user.id

    try:
        member = await update.effective_chat.get_member(
            user_id
        )

        return member.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )

    except Exception:
        return False
