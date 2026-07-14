# BT788 Toolkit Bot

A fast and simple Telegram utility bot built with **Python**, **python-telegram-bot**, **GitHub**, and **Railway**.

## Features

- 🔳 QR Code Generator
- 🔐 Secure Password Generator
- 🆔 UUID Generator
- 🔤 Text Case Converter
- 📊 Character Counter
- 🔠 Text Formatter

No external APIs are required. Everything runs locally.

---

## Project Structure

```text
BT788_BOT/
│
├── config.py
├── handlers.py
├── keyboards.py
├── main.py
├── utils.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/BT788_BOT.git
```

Go into the project:

```bash
cd BT788_BOT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Railway Deployment

Create the following environment variable:

```text
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Railway will automatically install the dependencies and run:

```text
python main.py
```

---

## Commands

| Command | Description |
|----------|-------------|
| /start | Open the main menu |
| /about | About the bot |

---

## License

MIT License
