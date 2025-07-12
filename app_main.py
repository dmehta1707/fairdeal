from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "FairDeal Bot is Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    return f"Received: {data['message']}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)