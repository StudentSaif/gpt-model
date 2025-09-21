# 🤖 Saif's Gemini AI Chat

A simple web application that integrates **Google's Gemini AI model** with a modern chat UI.
Built using **Flask (Python)** for the backend and **HTML/CSS/JavaScript + Bootstrap** for the frontend.

---

## 🚀 Features

* Clean **chat-style interface** with dark mode design
* Ask anything to Gemini AI and get instant responses
* Press **Enter** to send messages
* Backend built with **Flask** (keeps API key safe)
* Modern frontend using **Bootstrap 5**

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Backend:** Python (Flask)
* **AI Model:** Google Gemini (via `google-generativeai` SDK)

---

## 📂 Project Structure

```
├── app.py            # Flask backend
├── templates/
│   └── index.html    # Chat UI
├── static/
│   └── style.css     # Custom styles (optional)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone this repo**

   ```bash
   git clone https://github.com/your-username/gemini-ai-chat.git
   cd gemini-ai-chat
   ```

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Gemini API key**

   * Get your API key from [Google AI Studio](https://ai.google.dev/).
   * Open `app.py` and replace:

     ```python
     genai.configure(api_key="YOUR_API_KEY_HERE")
     ```

5. **Run the Flask app**

   ```bash
   python app.py
   ```

6. **Open in browser**
   Go to 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 requirements.txt

If you don’t already have one, create `requirements.txt` with:

```
flask
google-generativeai
```

---

## 📸 Screenshot (UI Example)

*(Add a screenshot of your running app here)*

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the **MIT License**.
