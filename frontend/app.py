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

    if response.status_code == 200:
            data = response.json()
            st.write(data["response"])
    else:
            st.error(f"Backend Error: {response.status_code}")
            st.write(response.text)