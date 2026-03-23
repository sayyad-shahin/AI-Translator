from gtts import gTTS
import os

def generate_audio(text, filename="outputs/output.mp3"):
    os.makedirs("outputs", exist_ok=True)
    tts = gTTS(text=text)
    tts.save(filename)
    return filename