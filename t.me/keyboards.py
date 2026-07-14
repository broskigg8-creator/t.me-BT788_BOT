from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🔳 QR Code", callback_data="qr"),
            InlineKeyboardButton("🔐 Password", callback_data="password"),
        ],
        [
            InlineKeyboardButton("🆔 UUID", callback_data="uuid"),
            InlineKeyboardButton("🔤 Case Converter", callback_data="case"),
        ],
        [
            InlineKeyboardButton("📊 Character Counter", callback_data="counter"),
            InlineKeyboardButton("🔠 Text Formatter", callback_data="formatter"),
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def back_menu():
    keyboard = [
        [
            InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def password_menu():
    keyboard = [
        [
            InlineKeyboardButton("8 Characters", callback_data="pass_8"),
            InlineKeyboardButton("12 Characters", callback_data="pass_12"),
        ],
        [
            InlineKeyboardButton("16 Characters", callback_data="pass_16"),
            InlineKeyboardButton("24 Characters", callback_data="pass_24"),
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="menu")
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def case_menu():
    keyboard = [
        [
            InlineKeyboardButton("UPPERCASE", callback_data="upper"),
            InlineKeyboardButton("lowercase", callback_data="lower"),
        ],
        [
            InlineKeyboardButton("Title Case", callback_data="title"),
            InlineKeyboardButton("Sentence case", callback_data="sentence"),
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="menu")
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def reply_menu():
    keyboard = [
        [KeyboardButton("/start"), KeyboardButton("/about")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )
