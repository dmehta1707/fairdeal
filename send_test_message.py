import requests

BOT_TOKEN = "8101949667:AAEglkb--2k--K7eiUQ-H1toM4xZ72GVhGs"
CHAT_ID = "-1002528960448"
TEXT = "🚀 Bot is now fully working!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": TEXT
}

res = requests.post(url, data=payload)
print(res.json())