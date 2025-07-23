from gtts import gTTS

LANG_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te"
}

def text_to_voice(text, lang="English"):
    try:
        lang_code = LANG_CODES.get(lang, "en")
        tts = gTTS(text=text, lang=lang_code)
        audio_path = "static/audio.mp3"
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        print("[gTTS Error]", e)
        return None



