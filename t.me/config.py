import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_NAME = "BT788 Toolkit Bot"
BOT_USERNAME = "@BT788_BOT"
BOT_VERSION = "1.0.0"

WELCOME_TEXT = f"""
👋 Welcome to {BOT_NAME}!

Your all-in-one utility assistant inside Telegram.

Available tools:

🔳 QR Code Generator
🔐 Password Generator
🆔 UUID Generator
🔤 Text Case Converter
📊 Character Counter
🔠 Text Formatter

Tap one of the buttons below to begin.
"""

ABOUT_TEXT = f"""
🤖 {BOT_NAME}

Version: {BOT_VERSION}

BT788 Toolkit Bot provides a collection of useful tools directly inside Telegram.

Features:

🔳 QR Code Generator
🔐 Password Generator
🆔 UUID Generator
🔤 Text Case Converter
📊 Character Counter
🔠 Text Formatter

Simple.
Fast.
Free.
"""
