# 🎯 Intelligent Excuse Generator (Multilingual)

A fun and smart web app that generates realistic or humorous excuses using an LLM (distilGPT2) and optionally speaks them out loud in **English**, **Hindi**, or **Telugu**.

---

## ✅ Features

- 🤖 AI-powered excuse generation using `distilgpt2`
- 🌍 Multilingual support (English, Hindi, Telugu)
- 🗣️ Text-to-speech voice output using `gTTS`
- 🌐 Clean Flask web interface
- 💾 History saved in JSON
- 🔁 Translations using `deep_translator`

---

## 📁 Folder Structure

ntelligent_excuse_generator/
├── app.py # Flask backend
├── llm_handler.py # LLM-based excuse generation (distilgpt2)
├── tts_handler.py # gTTS-based voice output
├── database.json # Stores generated excuses
├── requirements.txt # All Python dependencies
├── templates/
│ └── index.html # HTML frontend
└── static/
├── script.js # JS for AJAX and audio controls
└── style.css # Custom styling


---

## ⚙️ Installation Steps

### 1. 🧪 Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate

2. 📦 Install Dependencies

pip install -r requirements.txt
If playsound fails, skip it — we use HTML5 <audio> instead of native audio playback.

▶️ Run the App

python app.py
Visit: http://127.0.0.1:5000

🧠 How It Works
User enters a scenario, urgency, style, and proof option.

llm_handler.py uses distilgpt2 to generate an excuse.

The excuse is translated to the selected language using deep_translator.

tts_handler.py converts the final excuse to spoken audio via gTTS.

The excuse and voice file are returned to the frontend.

🗣️ Language Support
Language	Translated	Voice (gTTS)
English	✅	✅
Hindi	✅	✅
Telugu	✅	✅

✅ Example Prompts
"Why didn’t you do your homework?"

"Late submission excuse in formal tone"

"Missed the deadline due to power outage"

📦 Dependencies
flask

transformers

torch

gTTS

deep_translator

🚀 Future Scope
Save & filter history by language

Admin dashboard

Offline TTS fallback with better multilingual voices

📄 License
MIT License © 2025
