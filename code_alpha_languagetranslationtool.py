from google import genai
import streamlit as st
import time

# Page Title
st.title("🌐 AI Language Translator")
st.write(
    "Translate text easily into multiple languages using Google Gemini API."
)

# User Inputs
text_to_translate = st.text_area("Enter Text:", "")

col1, col2 = st.columns(2)
with col1:
  source_lang = st.selectbox(
      "Source Language:",
      [
          "English",
          "Urdu",
          "Sindhi",
          "Arabic",
          "French",
          "Spanish",
          "German",
          "Chinese",
      ],
  )
with col2:
  target_lang = st.selectbox(
      "Target Language:",
      [
          "Urdu",
          "English",
          "Sindhi",
          "Arabic",
          "French",
          "Spanish",
          "German",
          "Chinese",
      ],
  )

# Translate Button
if st.button("Translate"):
  if not text_to_translate.strip():
    st.warning("Please enter text to translate.")
  else:
    with st.spinner("Translating..."):
      try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

        prompt = (
            f"Translate the following text from {source_lang} to"
            f" {target_lang}. Only give the exact translation text without any"
            f" extra notes.\n\nText: {text_to_translate}"
        )

        response = None
        # Try primary model, if busy, try alternate stable model
        models_to_try = ["gemini-1.5-flash", "gemini-2.0-flash"]
        
        success = False
        for m in models_to_try:
          try:
            response = client.models.generate_content(
                model=m, contents=prompt
            )
            success = True
            break
          except Exception:
            continue

        if success and response:
          st.success("✨ Translated Text:")
          st.write(response.text)
        else:
          st.error("Servers are busy due to high demand. Please click Translate again in a few seconds!")

      except Exception as e:
        st.error(f"Error: {e}")
