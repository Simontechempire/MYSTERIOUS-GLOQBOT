from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.stylish import main_menu_keyboard, back_keyboard
from bot.utils.fonts import bold
from bot.utils.texts import MAIN_MENU_TEXT
from config import settings

router = Router(name="user")


@router.message(F.text == "🔙 Back to Menu")
async def back_to_menu(message: Message):
    await message.answer(MAIN_MENU_TEXT, reply_markup=main_menu_keyboard(), parse_mode="HTML")


@router.message(F.text == "🌌 AI Chat")
async def ai_chat(message: Message):
    text = f"""
🌌 {bold("AI Chat Module")}

Coming soon in full power mode.

• Multi-model intelligence
• Streaming responses
• Long context memory
• Voice & image support
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")


@router.message(F.text == "🎨 Content Studio")
async def content_studio(message: Message):
    text = f"""
🎨 {bold("Content Studio")}

Generate text, images, videos and more.
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")


@router.message(F.text == "🧠 Memory")
async def memory_module(message: Message):
    text = f"""
🧠 {bold("Memory System")}

Long-term personalized memory for every user.
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")


@router.message(F.text == "⚡ Agents")
async def agents_module(message: Message):
    text = f"""
⚡ {bold("Autonomous Agents")}

Multi-step planning • Tool calling • Proactive actions
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")


@router.message(F.text == "🛡️ Community")
async def community_module(message: Message):
    text = f"""
🛡️ {bold("Community Suite")}

Advanced group moderation, analytics and engagement tools.
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")


@router.message(F.text == "💹 Crypto Desk")
async def crypto_module(message: Message):
    text = f"""
💹 {bold("Crypto Desk")}

Portfolio tracking • Alerts • Signals
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")


@router.message(F.text == "👤 Profile")
@router.message(Command("profile"))
async def profile(message: Message):
    user = message.from_user
    text = f"""
👤 {bold("Your Profile")}

ID: <code>{user.id}</code>
Name: {user.full_name}
Username: @{user.username or "none"}

Owner of this bot: {settings.OWNER_NAME}
@{settings.OWNER_USERNAME}
"""
    await message.answer(text, reply_markup=back_keyboard(), parse_mode="HTML")
