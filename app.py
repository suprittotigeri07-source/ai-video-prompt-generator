import streamlit as st
import json
from prompt_engine import generate_video_prompt

st.set_page_config(page_title="AI Video Prompt Generator", layout="centered")

st.title("🎥 AI Prompt-Based Video Concept Generator")
st.write("Generate scene-by-scene video prompts for ads using AI-style logic.")

brand = st.text_input("Brand Name")
product = st.text_input("Product / Service")

platform = st.selectbox(
    "Target Platform",
    ["Instagram Reels", "YouTube Shorts", "Facebook Ads"]
)

tone = st.selectbox(
    "Video Tone",
    ["Cinematic", "Minimal", "UGC", "Storytelling"]
)

if st.button("Generate Video Prompt"):
    if brand and product:
        prompts = generate_video_prompt(brand, product, platform, tone)

        st.subheader("🎬 Generated Video Scenes")
        st.json(prompts)

        with open("sample_output.json", "w") as f:
            json.dump(prompts, f, indent=4)

        st.success("Video prompt generated successfully!")
    else:
        st.error("Please enter Brand and Product name.")
