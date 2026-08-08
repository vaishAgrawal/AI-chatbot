import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask Anything")

if st.button("Send"):

    response = requests.post(
        f"{BACKEND_URL}",
        json={"message": user_input}
    )

    st.write(response.json()["response"])