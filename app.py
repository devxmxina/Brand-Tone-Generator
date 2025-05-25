import streamlit as st
from generator import generate_brand_tone_content
from prompts import brand_tone_prompts

st.set_page_config(page_title="Brand Tone Generator", page_icon="💬", layout="centered")
st.title("💬 Brand-Tone Content Generator")

api_key = st.text_input("🔑 Enter your Google API Key", type="password")
brand_description = st.text_area("📝 Enter your brand description")
tone = st.selectbox("🎭 Choose brand tone", list(brand_tone_prompts.keys()))
language = st.selectbox("🌐 Choose output language", ["English", "Russian", "Spanish", "French"])

if st.button("Generate"):
    if not api_key:
        st.error("Please enter your API key.")
        st.stop()
    if not brand_description:
        st.error("Please enter brand description.")
        st.stop()

    with st.spinner("Generating content..."):
        try:
            content = generate_brand_tone_content(
                api_key=api_key,
                brand_description=brand_description,
                tone=brand_tone_prompts[tone],
                language=language
            )
            st.markdown(f"### ✨ {tone} Style Output:\n\n{content}")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")