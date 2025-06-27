import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk AI", page_icon="None", layout="centered")

st.title(" TailorTalk - Book Appointments")
st.subheader("Let me schedule your meetings!!")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Ask me to book an appointment with date/time...")

if user_input:
    st.session_state.history.append(("You", user_input))
    with st.spinner("Thinking..."):
        try:
            response = requests.post("http://localhost:8000/chat", json={"message": user_input})
            if response.status_code == 200:
                reply = response.json()["response"]
            else:
                reply = "⚠️ Error from backend."
        except Exception as e:
            reply = f" Backend error: {e}"
    st.session_state.history.append(("Bot", reply))

for sender, msg in st.session_state.history:
    st.write(f"**{sender}:** {msg}")

