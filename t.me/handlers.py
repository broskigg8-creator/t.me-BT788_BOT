from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from config import (
    WELCOME_TEXT,
    ABOUT_TEXT,
)

from keyboards import (
    main_menu,
    back_menu,
    password_menu,
    case_menu,
)

from utils import (
    generate_qr,
    generate_password,
    generate_uuid,
    count_text,
    to_upper,
    to_lower,
    to_title,
    to_sentence,
    format_bold,
)


# ======================================================
# START COMMAND
# ======================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()

    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=main_menu()
    )


# ======================================================
# ABOUT COMMAND
# ======================================================

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        ABOUT_TEXT,
        reply_markup=back_menu()
    )


# ======================================================
# BUTTON HANDLER
# ======================================================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # ---------------- MAIN MENU ----------------

    if data == "menu":

        context.user_data.clear()

        await query.edit_message_text(
            WELCOME_TEXT,
            reply_markup=main_menu()
        )

        return

    # ---------------- ABOUT ----------------

    if data == "about":

        await query.edit_message_text(
            ABOUT_TEXT,
            reply_markup=back_menu()
        )

        return

    # ---------------- QR ----------------

    if data == "qr":

        context.user_data.clear()
        context.user_data["mode"] = "qr"

        await query.edit_message_text(
            "🔳 Send the text or URL you want to convert into a QR Code.",
            reply_markup=back_menu()
        )

        return

    # ---------------- PASSWORD ----------------

    if data == "password":

        context.user_data.clear()

        await query.edit_message_text(
            "🔐 Choose your password length.",
            reply_markup=password_menu()
        )

        return

    if data.startswith("pass_"):

        length = int(data.split("_")[1])

        password = generate_password(length)

        await query.edit_message_text(
            f"🔐 Your Password\n\n`{password}`",
            parse_mode="Markdown",
            reply_markup=password_menu()
        )

        return

    # ---------------- UUID ----------------

    if data == "uuid":

        uid = generate_uuid()

        await query.edit_message_text(
            f"🆔 UUID Generated\n\n`{uid}`",
            parse_mode="Markdown",
            reply_markup=back_menu()
        )

        return

    # ---------------- CHARACTER COUNTER ----------------

    if data == "counter":

        context.user_data.clear()
        context.user_data["mode"] = "counter"

        await query.edit_message_text(
            "📊 Send any text.",
            reply_markup=back_menu()
        )

        return

    # ---------------- FORMATTER ----------------

    if data == "formatter":

        context.user_data.clear()
        context.user_data["mode"] = "formatter"

        await query.edit_message_text(
            "🔠 Send your text.",
            reply_markup=back_menu()
        )

        return

    # ---------------- CASE MENU ----------------

    if data == "case":

        context.user_data.clear()

        await query.edit_message_text(
            "Choose how you want to convert your text.",
            reply_markup=case_menu()
        )

        return

    if data == "upper":

        context.user_data["mode"] = "upper"

        await query.edit_message_text(
            "Send the text.",
            reply_markup=back_menu()
        )

        return

    if data == "lower":

        context.user_data["mode"] = "lower"

        await query.edit_message_text(
            "Send the text.",
            reply_markup=back_menu()
        )

        return

    if data == "title":

        context.user_data["mode"] = "title"

        await query.edit_message_text(
            "Send the text.",
            reply_markup=back_menu()
        )

        return

    if data == "sentence":

        context.user_data["mode"] = "sentence"

        await query.edit_message_text(
            "Send the text.",
            reply_markup=back_menu()
        )

        return


# ======================================================
# TEXT HANDLER
# ======================================================

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if "mode" not in context.user_data:

        await update.message.reply_text(
            "Choose a tool first.",
            reply_markup=main_menu()
        )

        return

    mode = context.user_data["mode"]

    text = update.message.text.strip()

    # QR CODE

    if mode == "qr":

        qr = generate_qr(text)

        await update.message.reply_photo(
            photo=qr,
            caption="✅ QR Code Generated Successfully.",
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return

    # CHARACTER COUNTER

    if mode == "counter":

        result = count_text(text)

        await update.message.reply_text(
            f"📊 Text Analysis\n\n"
            f"Characters: {result['characters']}\n"
            f"Words: {result['words']}",
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return

    # FORMATTER

    if mode == "formatter":

        formatted = format_bold(text)

        await update.message.reply_text(
            formatted,
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return
    # UPPERCASE

    if mode == "upper":

        converted = to_upper(text)

        await update.message.reply_text(
            converted,
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return

    # LOWERCASE

    if mode == "lower":

        converted = to_lower(text)

        await update.message.reply_text(
            converted,
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return

    # TITLE CASE

    if mode == "title":

        converted = to_title(text)

        await update.message.reply_text(
            converted,
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return

    # SENTENCE CASE

    if mode == "sentence":

        converted = to_sentence(text)

        await update.message.reply_text(
            converted,
            reply_markup=back_menu()
        )

        context.user_data.clear()

        return

    await update.message.reply_text(
        "Please choose a tool from the menu first.",
        reply_markup=main_menu()
    )


# ======================================================
# UNKNOWN COMMAND
# ======================================================

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "❌ Unknown command.\n\nUse /start to open the main menu."
    )


# ======================================================
# ERROR HANDLER
# ======================================================

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):

    print(f"Error: {context.error}")


# ======================================================
# REGISTER ALL HANDLERS
# ======================================================

def get_handlers():

    return [

        CommandHandler(
            "start",
            start
        ),

        CommandHandler(
            "about",
            about
        ),

        CallbackQueryHandler(
            buttons
        ),

        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_handler
        ),

        MessageHandler(
            filters.COMMAND,
            unknown
        ),

    ]
