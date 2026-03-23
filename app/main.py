import streamlit as st
from translator import translate_text
from tts import generate_audio
from stt import speech_to_text
import os

# Page config
st.set_page_config(page_title="AI Voice Translator Pro", layout="centered")

st.title("🌍 AI Multilingual Voice Studio")

# Mode selection
mode = st.radio("Choose Input Type:", ["Text", "Voice"])

# Language selection
lang_map = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Hinglish": "hin_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Spanish": "spa_Latn",
    "Arabic": "arb_Arab",
    "Chinese": "zho_Hans"
}

target_lang = st.selectbox("🌐 Target Language", list(lang_map.keys()))

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# ------------------ TEXT MODE ------------------ #
if mode == "Text":
    text = st.text_area("✍️ Enter Text")

    if st.button("🚀 Translate & Generate Audio"):
        if text.strip() == "":
            st.warning("⚠️ Please enter text first!")
        else:
            with st.spinner("Processing... ⏳"):
                translated = translate_text(text, lang_map[target_lang])

                st.subheader("📘 Translated Text:")
                st.success(translated)

                audio_path = "outputs/output.mp3"   # ✅ FIXED
                generate_audio(translated, audio_path)

                st.audio(audio_path)

                with open(audio_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Audio",
                        f,
                        file_name="translated_audio.mp3"   # ✅ FIXED
                    )

# ------------------ VOICE MODE ------------------ #
elif mode == "Voice":
    audio_file = st.file_uploader("🎤 Upload Voice File", type=["wav", "mp3"])

    if audio_file is not None:
        temp_path = "outputs/temp.wav"

        # Save uploaded file
        with open(temp_path, "wb") as f:
            f.write(audio_file.read())

        with st.spinner("Converting speech to text... ⏳"):
            text = speech_to_text(temp_path)

        st.subheader("📝 Recognized Text:")
        st.info(text)

        if text.strip() != "":
            with st.spinner("Translating & Generating Audio... ⏳"):
                translated = translate_text(text, lang_map[target_lang])

                st.subheader("📘 Translated Text:")
                st.success(translated)

                audio_path = "outputs/output.mp3"   # ✅ FIXED
                generate_audio(translated, audio_path)

                st.audio(audio_path)

                with open(audio_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Audio",
                        f,
                        file_name="translated_audio.mp3"   # ✅ FIXED
                    )
        else:
            st.error("❌ Could not detect speech properly. Try again.")