import streamlit as st
import requests

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask Anything")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    )

    st.write(response.json()["response"])