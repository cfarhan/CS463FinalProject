from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyDclOtu0ERkZ6Z8AJxqxf0ty25r-1Z9DMs"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY

@app.route('/')
def default():
    return "Hello, world"

@app.route('/question', methods=['POST'])
def ask_gemini():
    data = request.get_json()
    prompt1 = "You are the judge on the results of a quiz. The quiz is related to my favourite Pokemon. The answers are as follows in a list format: [Garchomp, Gardevoir, Charizard, Moltres, Zapdos, Glaceon, Rayquaza, Eevee, Dragonair]." 
    prompt2 = "I am providing you the users input for a guess, check if it matches anything in my list. You can use fuzzy matching and ignore capitalization to match their answer. Just reply with correct or incorrect, and give a hint if its incorrect. Here is the list: "
    user_input = data.get("quiz_response")
    
    if not user_input:
        return jsonify({"error": "Missing 'quiz_response' parameter"}), 400
    
    payload = {
        "contents": [{
        "parts":[{"text": prompt1 + prompt2 + user_input}]
    }]
   }
    params = {"key": GEMINI_API_KEY}
    
    response = requests.post(GEMINI_API_URL, json=payload, params=params)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch response from Google Gemini"}), response.body
    
    gemini_response = response.json()
    answer = gemini_response.get('candidates')[0].get('content').get("parts")[0].get('text')
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)