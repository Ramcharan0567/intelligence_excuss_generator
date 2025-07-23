from flask import Flask, render_template, request, jsonify
from llm_handler import generate_excuse
from tts_handler import text_to_voice
from deep_translator import GoogleTranslator
from datetime import datetime
import json
import os

app = Flask(__name__, static_url_path="/static")
DB_FILE = "database.json"

# Language mapping
LANG_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te"
}

# Translate English to target language
def translate_text(text, target_lang="English"):
    try:
        target_code = LANG_CODES.get(target_lang, "en")
        if target_code == "en":
            return text
        return GoogleTranslator(source='en', target=target_code).translate(text)
    except Exception as e:
        print("[Translation Error]", e)
        return text  # fallback to original

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    scenario = data.get("scenario", "")
    urgency = data.get("urgency", "")
    style = data.get("style", "")
    proof = data.get("proof", "")
    language = data.get("language", "English")

    # Generate in English
    excuse_en = generate_excuse(scenario, urgency, style, proof)

    # Translate if needed
    excuse = translate_text(excuse_en, language)

    # Save to DB
    entry = {
        "input": data,
        "output": excuse,
        "timestamp": datetime.now().isoformat()
    }
    history = []
    if os.path.exists(DB_FILE):
        history = json.load(open(DB_FILE))
    history.append(entry)
    json.dump(history, open(DB_FILE, "w"), indent=2)

    # Generate voice
    audio_path = text_to_voice(excuse, lang=language)
    if audio_path is None:
        return jsonify({"excuse": excuse, "audio": None})

    return jsonify({"excuse": excuse, "audio": "/" + audio_path})

@app.route("/history")
def history():
    if not os.path.exists(DB_FILE):
        return jsonify([])
    return jsonify(json.load(open(DB_FILE)))

if __name__ == "__main__":
    app.run(debug=True)


