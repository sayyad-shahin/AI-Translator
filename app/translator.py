from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st

@st.cache_resource
def load_model():
    model_name = "facebook/nllb-200-distilled-600M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

def translate_text(text, target_lang_code):
    inputs = tokenizer(text, return_tensors="pt")

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_lang_code)
    )

    return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)