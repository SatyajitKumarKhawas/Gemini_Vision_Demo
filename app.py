from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

# Function to get Gemini response
def get_gemini_response(user_input, image):
    if image is not None:
        image_data = {
            "mime_type": image.type,
            "data": image.getvalue()
        }
        if user_input.strip() != "":
            result = model.generate_content([user_input, image_data])
        else:
            result = model.generate_content([image_data])
    else:
        result = model.generate_content(user_input)
    
    return result.text

# Streamlit UI
st.set_page_config(
    page_title="Q&A DEMO",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-7t5AkQU2WfIb4fC2lyOtPrko_Ku9lQkxnw&s"
)

st.title("🖼️ Gemini Image + Text Demo")

# Input fields
user_input = st.text_input("Enter your question (optional):")
uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

# Submit button
if st.button("Ask Gemini"):
    if user_input.strip() == "" and uploaded_image is None:
        st.warning("Please provide at least text or an image.")
    else:
        with st.spinner("Generating response..."):
            response = get_gemini_response(user_input, uploaded_image)
        st.subheader("🤖 Gemini's Response:")
        st.write(response)
