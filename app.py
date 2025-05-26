from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Simple rule-based responses
responses = {
    "hello": "Hi there! How are you feeling today?",
    "sad": "I'm sorry you're feeling this way. Try taking a deep breath and remember you're not alone.",
    "anxious": "It's okay to feel anxious sometimes. Would you like to try a 3-minute breathing exercise?",
    "stress": "Maybe a short walk or journaling could help ease your stress.",
    "bye": "Take care of yourself! I'm here whenever you want to talk.",
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message", "").lower()
    reply = "I'm here to listen. Can you tell me more?"  # Default reply
    for keyword in responses:
        if keyword in user_msg:
            reply = responses[keyword]
            break
    return jsonify({"reply": reply})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
