import google.generativeai as genai
import streamlit as st

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

# Initialize Gemini API using Streamlit Secrets
try:
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
  pass

# Translate Button
if st.button("Translate"):
  if not text_to_translate.strip():
    st.warning("Please enter text to translate.")
  else:
    with st.spinner("Translating..."):
      try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = (
            f"Translate the following text from {source_lang} to"
            f" {target_lang}. Only give the exact translation text without any"
            f" extra notes.\n\nText: {text_to_translate}"
        )

        response = model.generate_content(prompt)

        st.success("✨ Translated Text:")
        st.write(response.text)
      except Exception as e:
        st.error(
            f"Error: {e}. Please check if GEMINI_API_KEY is added in Streamlit"
            " Secrets."
        )
