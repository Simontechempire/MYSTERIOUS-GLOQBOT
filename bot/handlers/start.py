from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatMemberStatus

from config import settings
from bot.keyboards.stylish import force_join_keyboard, main_menu_keyboard
from bot.utils.texts import WELCOME, FORCE_JOIN_TEXT, SUCCESS_JOIN_TEXT, NOT_MEMBER_TEXT, ABOUT_TEXT, HELP_TEXT

router = Router(name="start")


async def check_membership(bot: Bot, user_id: int) -> bool:
    allowed = {
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.CREATOR,
        ChatMemberStatus.RESTRICTED,
    }
    for chat in settings.force_join_chats:
        try:
            member = await bot.get_chat_member(chat_id=f"@{chat}", user_id=user_id)
            if member.status not in allowed:
                return False
        except Exception:
            return False
    return True


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    user = message.from_user

    if user.id in settings.admin_ids:
        await message.answer(WELCOME, reply_markup=main_menu_keyboard(), parse_mode="HTML")
        return

    if await check_membership(bot, user.id):
        await message.answer(WELCOME, reply_markup=main_menu_keyboard(), parse_mode="HTML")
    else:
        await message.answer(FORCE_JOIN_TEXT, reply_markup=force_join_keyboard(), parse_mode="HTML")


@router.callback_query(F.data == "check_force_join")
async def check_force_join_callback(callback: CallbackQuery, bot: Bot):
    if await check_membership(bot, callback.from_user.id):
        await callback.message.edit_text(SUCCESS_JOIN_TEXT, parse_mode="HTML")
        await callback.message.answer(WELCOME, reply_markup=main_menu_keyboard(), parse_mode="HTML")
        await callback.answer("✅ Access granted!")
    else:
        await callback.answer(NOT_MEMBER_TEXT, show_alert=True)


@router.message(Command("help"))
@router.message(F.text == "📖 Help")
async def cmd_help(message: Message):
    await message.answer(HELP_TEXT, parse_mode="HTML")


@router.message(Command("about"))
@router.message(F.text == "ℹ️ About")
async def cmd_about(message: Message):
    await message.answer(ABOUT_TEXT, parse_mode="HTML")
