import streamlit as st
from deep_translator import GoogleTranslator

# Page Title
st.title("🌐 Language Translator Tool")
st.write("Translate text easily into multiple languages.")

# Language Options Mapping
languages = {
    'English': 'en',
    'Urdu': 'ur',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-CN',
    'Arabic': 'ar'

}

# User Inputs
text_to_translate = st.text_area("Enter Text:", "")
source_lang_name = st.selectbox("Source Language:", list(languages.keys()), index=0)
target_lang_name = st.selectbox("Target Language:", list(languages.keys()), index=1)

# Translate Button
if st.button("Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter text to translate.")
    else:
        try:
            source_code = languages[source_lang_name]
            target_code = languages[target_lang_name]

            time.sleep(1)
            translated = GoogleTranslator(source=source_code, target=target_code).translate(text_to_translate)
            
            st.success("### Translated Text:")
            st.write(translated)
        except Exception as e:
            st.error(f"Error: {str(e)}")
