from config import settings
from .fonts import bold, fancy

BOT_NAME = "MYSTERIOUS GLOQBOT"
OWNER_NAME = settings.OWNER_NAME
OWNER_USERNAME = settings.OWNER_USERNAME

WELCOME = f"""
✨ {bold(BOT_NAME)} ✨

Welcome to the most powerful AI operating system on Telegram.

Owner: {OWNER_NAME}
Contact: @{OWNER_USERNAME}

Choose an option below ⬇️
"""

FORCE_JOIN_TEXT = f"""
🔒 {bold("ACCESS RESTRICTED")}

To unlock {fancy(BOT_NAME)} you must join all required channels & groups:

1️⃣ Queen Tech Channel
2️⃣ Queen Tech Group  
3️⃣ Simon Tech

After joining, press ✅ I HAVE JOINED
"""

MAIN_MENU_TEXT = f"""
🌌 {bold(BOT_NAME)} — Main Menu

Your personal AI powerhouse is ready.
Select a module below.
"""

ABOUT_TEXT = f"""
ℹ️ {bold("About")} {fancy(BOT_NAME)}

The ultimate multi-agent AI system living inside Telegram.

• Multi-modal intelligence
• Long-term memory
• Autonomous agents
• Content studio
• Community tools
• Crypto desk

Owner: {OWNER_NAME}
Username: @{OWNER_USERNAME}
"""

HELP_TEXT = f"""
📖 {bold("Help & Commands")}

/start — Open main menu
/help — Show this help
/about — About the bot
/profile — Your profile
/admin — Admin panel (owner only)

Use the stylish buttons below for full power.
"""

NOT_MEMBER_TEXT = "❌ You are still not a member of all required chats. Please join and try again."
SUCCESS_JOIN_TEXT = f"✅ Access granted! Welcome to {bold(BOT_NAME)}"
