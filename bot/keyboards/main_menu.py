from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🧠 AI Tools", callback_data="ai_tools"),
            InlineKeyboardButton("🤖 Agents", callback_data="agents"),
        ],
        [
            InlineKeyboardButton("🎨 Creative", callback_data="creative"),
            InlineKeyboardButton("🔬 Research", callback_data="research"),
        ],
        [
            InlineKeyboardButton("👥 Community", callback_data="community"),
            InlineKeyboardButton("💼 Business", callback_data="business"),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
