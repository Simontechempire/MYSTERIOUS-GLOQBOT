from telegram import InlineKeyboardButton


def stylish_button(text: str, callback_data: str):
    return InlineKeyboardButton(
        text=text,
        callback_data=callback_data
    )
