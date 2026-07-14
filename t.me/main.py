from telegram.ext import Application

from config import BOT_TOKEN
from handlers import (
    get_handlers,
    error_handler,
)


def main():

    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN environment variable is not set."
        )

    application = Application.builder().token(BOT_TOKEN).build()

    for handler in get_handlers():
        application.add_handler(handler)

    application.add_error_handler(error_handler)

    print("====================================")
    print(" BT788 Toolkit Bot is now running...")
    print("====================================")

  application.run_polling()


if __name__ == "__main__":
    main()
