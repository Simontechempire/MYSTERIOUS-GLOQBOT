from telegram import InlineKeyboardMarkup

from .stylish import stylish_button


def main_menu():
    keyboard = [
        [
            stylish_button("🧠 AI 𝗧𝗼𝗼𝗹𝘀", "ai_tools"),
            stylish_button("🤖 𝗔𝗴𝗲𝗻𝘁𝘀", "agents"),
        ],
        [
            stylish_button("🎨 𝗖𝗿𝗲𝗮𝘁𝗶𝘃𝗲", "creative"),
            stylish_button("🔬 𝗥𝗲𝘀𝗲𝗮𝗿𝗰𝗵", "research"),
        ],
        [
            stylish_button("👥 𝗖𝗼𝗺𝗺𝘂𝗻𝗶𝘁𝘆", "community"),
            stylish_button("💼 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀", "business"),
        ],
        [
            stylish_button("⚙️ 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀", "settings"),
            stylish_button("ℹ️ 𝗔𝗯𝗼𝘂𝘁", "about"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
