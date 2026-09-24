from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import settings


def force_join_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📢 Queen Tech Channel", url=f"https://t.me/{settings.FORCE_JOIN_CHANNEL}"))
    builder.row(InlineKeyboardButton(text="👥 Queen Tech Group", url=f"https://t.me/{settings.FORCE_JOIN_GROUP}"))
    builder.row(InlineKeyboardButton(text="🔥 Simon Tech", url=f"https://t.me/{settings.FORCE_JOIN_SIMON}"))
    builder.row(InlineKeyboardButton(text="✅ I HAVE JOINED", callback_data="check_force_join"))
    return builder.as_markup()


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="🌌 AI Chat"), KeyboardButton(text="🎨 Content Studio"))
    builder.row(KeyboardButton(text="🧠 Memory"), KeyboardButton(text="⚡ Agents"))
    builder.row(KeyboardButton(text="🛡️ Community"), KeyboardButton(text="💹 Crypto Desk"))
    builder.row(KeyboardButton(text="👤 Profile"), KeyboardButton(text="ℹ️ About"))
    builder.row(KeyboardButton(text="📖 Help"))
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Select a powerful module...")


def back_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="🔙 Back to Menu"))
    return builder.as_markup(resize_keyboard=True)


def admin_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="📊 Stats"), KeyboardButton(text="📢 Broadcast"))
    builder.row(KeyboardButton(text="👥 Users"), KeyboardButton(text="⚙️ Settings"))
    builder.row(KeyboardButton(text="🔙 Back to Menu"))
    return builder.as_markup(resize_keyboard=True)
