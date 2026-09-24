from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from bot.filters.is_owner import IsOwner
from bot.keyboards.stylish import admin_keyboard
from bot.utils.fonts import bold
from config import settings

router = Router(name="admin")


@router.message(Command("admin"), IsOwner())
async def admin_panel(message: Message):
    text = f"""
⚙️ {bold("Admin Panel")}

Owner: {settings.OWNER_NAME}
Username: @{settings.OWNER_USERNAME}

Select an option:
"""
    await message.answer(text, reply_markup=admin_keyboard(), parse_mode="HTML")


@router.message(F.text == "📊 Stats", IsOwner())
async def admin_stats(message: Message):
    await message.answer("📊 Stats module coming soon.", reply_markup=admin_keyboard())


@router.message(F.text == "📢 Broadcast", IsOwner())
async def admin_broadcast(message: Message):
    await message.answer("📢 Broadcast system coming soon.", reply_markup=admin_keyboard())


@router.message(F.text == "👥 Users", IsOwner())
async def admin_users(message: Message):
    await message.answer("👥 User management coming soon.", reply_markup=admin_keyboard())


@router.message(F.text == "⚙️ Settings", IsOwner())
async def admin_settings(message: Message):
    await message.answer("⚙️ Settings coming soon.", reply_markup=admin_keyboard())
