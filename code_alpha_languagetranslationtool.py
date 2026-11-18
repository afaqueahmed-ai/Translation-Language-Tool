from google import genai
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Language Translator Pro", page_icon="🌐", layout="centered"
)

# App Title & Description
st.title("🌐 AI Language Translator Pro")
st.write(
    "Translate text smoothly across 30+ languages using Google Gemini API with"
    " automated fallback protection."
)

# 30+ Popular Languages List
LANGUAGES = [
    "English",
    "Urdu",
    "Sindhi",
    "Arabic",
    "French",
    "Spanish",
    "German",
    "Chinese (Mandarin)",
    "Hindi",
    "Punjabi",
    "Pashto",
    "Balochi",
    "Persian (Farsi)",
    "Turkish",
    "Japanese",
    "Korean",
    "Italian",
    "Portuguese",
    "Russian",
    "Bengali",
    "Indonesian",
    "Malay",
    "Vietnamese",
    "Thai",
    "Dutch",
    "Greek",
    "Polish",
    "Swedish",
    "Romanian",
    "Ukrainian",
]

# User Inputs
text_to_translate = st.text_area(
    "Enter text to translate:", "", placeholder="Type anything here..."
)

col1, col2 = st.columns(2)
with col1:
  source_lang = st.selectbox("Source Language:", LANGUAGES)
with col2:
  target_lang = st.selectbox("Target Language:", LANGUAGES)

# Translate Button
if st.button("Translate Now", type="primary"):
  if not text_to_translate.strip():
    st.warning("⚠️ Please enter some text to translate.")
  else:
    with st.spinner("Translating via Gemini AI..."):
      try:
        # Initialize Gemini Client using Streamlit Secrets (24/7 Secure)
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

        prompt = (
            f"Translate the following text accurately from {source_lang} to"
            f" {target_lang}. Provide ONLY the translated text without any"
            f" introductory notes, quotation marks, or explanations.\n\nText:"
            f" {text_to_translate}"
        )

        # Multi-Model Fallback List to handle high traffic / 503 errors seamlessly
        models_to_try = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-3.8-flash",
        ]

        response = None
        success = False

        for model_name in models_to_try:
          try:
            response = client.models.generate_content(
                model=model_name, contents=prompt
            )
            if response and response.text:
              success = True
              break
          except Exception:
            # Try next model if current one is overloaded or unavailable
            continue

        if success and response:
          st.success("✨ Translated Text:")
          st.code(response.text, language=None)
        else:
          st.error(
              "🚨 Servers are currently experiencing high demand. Please click"
              " 'Translate Now' again in a few seconds!"
          )

      except Exception as e:
        st.error(
            f"Error: {e}. Please make sure GEMINI_API_KEY is correctly added"
            " in your Streamlit Cloud Secrets."
        )
