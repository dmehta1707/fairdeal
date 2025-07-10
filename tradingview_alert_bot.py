
from flask import Flask, request
import requests

app = Flask(__name__)

# ⛔ Replace below with your own info:
BOT_TOKEN = '8011327420:AAEaHJzYrmehRcGKOn_FqY19WTlVw9mHLPI_here'
CHAT_ID = 5036794463


def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get("symbol", "N/A")
    action = data.get("direction", "N/A")
    tf = data.get("timeframe", "N/A")

    message = f"📈 {symbol} | {tf} min\n🟢 Signal: {action.upper()}"
    send_telegram_message(message)

    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
