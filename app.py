import streamlit as st
from model_helper import predict
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Car Damage Checker", page_icon="🚗", layout="centered")

# Cute styling
st.markdown("""
    <style>
    .main {background-color: #fff3f6;}
    .stButton>button {
        background-color: #ff6f91;
        color: white;
        border-radius: 10px;
        padding: 6px 12px;
        font-family: 'Comic Sans MS', sans-serif;
    }
    .stButton>button:hover {background-color: #ff4d73;}
    .prediction-box {
        background-color: #ffe6ec;
        padding: 8px;
        border-radius: 8px;
        border: 2px solid #ff8ba7;
        margin-top: 10px;
    }
    .title {color: #ff4d73; font-size: 28px; text-align: center; font-family: 'Comic Sans MS', sans-serif;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚗 Car Damage Checker</div>', unsafe_allow_html=True)
st.write("Upload a car pic! 📸")

uploaded_file = st.file_uploader("", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Car! 🚘", use_container_width=True)
    
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if st.button("Check Damage 🔍"):
        with st.spinner("Checking..."):
            prediction = predict(image_path)
            st.info(f"Status: {prediction}")
        
        if os.path.exists(image_path):
            os.remove(image_path)
