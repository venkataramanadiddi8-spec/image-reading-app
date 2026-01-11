from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
import streamlit as st

# choose the title
st.title("Image application")

# Upload a file
uploaded_file = st.file_uploader("Upload an image",
 type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(Image.open(uploaded_file))
prompt = st.text_input("Enter the text")

# Use genai skill
if st.button("GET RESPONSE"):
    img = Image.open(uploaded_file)
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt,img])
    st.success(response.text)