from flask import Flask, request
import requests

app = Flask(_name_)

@app.route('/')
def home():
    return "FairDeal Bot is Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)

    # Extract message from TradingView alert JSON
    message = data.get('message', '📢 TradingView Alert Received!')

    # Telegram bot credentials
    BOT_TOKEN = "8101949667:AAEglkb--2k--K7eiUQ-H1toM4xZ72GVhGs"
    CHAT_ID = -1002528960448

    # Send message to Telegram group
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(telegram_url, json=payload)

    return f"Received: {message}", 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
