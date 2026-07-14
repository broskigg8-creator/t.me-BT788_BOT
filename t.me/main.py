from telegram.ext import Application

from config import BOT_TOKEN
from handlers import get_handlers, error_handler


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing. Please set it in your Railway Environment Variables."
        )

    application = Application.builder().token(BOT_TOKEN).build()

    # Register all handlers
    for handler in get_handlers():
        application.add_handler(handler)

    # Register error handler
    application.add_error_handler(error_handler)

    print("=" * 50)
    print("🤖 BT788 Toolkit Bot is running...")
    print("=" * 50)

    application.run_polling()


if __name__ == "__main__":
    main()
