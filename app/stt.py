import whisper
import streamlit as st

@st.cache_resource
def load_model():
    return whisper.load_model("tiny")  # fast

model = load_model()

def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]