import io
import uuid
import random
import string

import qrcode


# -----------------------------
# QR CODE GENERATOR
# -----------------------------
def generate_qr(data: str):
    """
    Generate a QR code image from text.
    Returns a BytesIO object.
    """

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer


# -----------------------------
# PASSWORD GENERATOR
# -----------------------------
def generate_password(length=12):
    """
    Generate a secure random password.
    """

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()-_=+"
    )

    return "".join(random.SystemRandom().choice(characters) for _ in range(length))


# -----------------------------
# UUID GENERATOR
# -----------------------------
def generate_uuid():
    """
    Generate a Version 4 UUID.
    """

    return str(uuid.uuid4())


# -----------------------------
# CHARACTER COUNTER
# -----------------------------
def count_text(text: str):
    """
    Count characters and words.
    """

    return {
        "characters": len(text),
        "words": len(text.split())
    }


# -----------------------------
# TEXT CASE CONVERTER
# -----------------------------
def to_upper(text: str):
    return text.upper()


def to_lower(text: str):
    return text.lower()


def to_title(text: str):
    return text.title()


def to_sentence(text: str):
    if not text:
        return text

    return text[0].upper() + text[1:].lower()


# -----------------------------
# SIMPLE UNICODE FORMATTER
# -----------------------------
BOLD_MAP = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
    "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
)

def format_bold(text: str):
    return text.translate(BOLD_MAP)
