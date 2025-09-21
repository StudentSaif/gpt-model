from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure API key (better to use environment variable for security)
genai.configure(api_key="your_api_key")

model = genai.GenerativeModel("AI_Model")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("question", "")

    response = model.generate_content(user_input)
    return jsonify({"answer": response.text})

if __name__ == "__main__":
    app.run(debug=True)