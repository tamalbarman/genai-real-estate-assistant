import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="AI Real Estate Assistant",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AI Real Estate Assistant")
st.caption("Find properties using natural language")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

if "state" not in st.session_state:
    st.session_state.state = {}

# Sidebar
with st.sidebar:

    st.header("🔎 Current Search")

    if st.session_state.state:
        st.json(st.session_state.state)
    else:
        st.write("No filters yet")

    if st.button("Reset Chat"):
        st.session_state.history = []
        st.session_state.state = {}
        st.rerun()

    st.divider()

    st.markdown("### Example Queries")
    st.write("• 2 BHK in Kolkata under 1 crore")
    st.write("• Apartments in Delhi under 80 lakh")
    st.write("• 3 BHK villa in Mumbai with gym")

# Chat history
for role, message in st.session_state.history:
    with st.chat_message(role):
        st.markdown(message)

# User input
user_input = st.chat_input("Ask about properties...")

if user_input:

    # show user message
    st.session_state.history.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # call API
    with st.chat_message("assistant"):

        with st.spinner("Searching properties..."):

            response = requests.post(
                API_URL,
                json={"message": user_input}
            )

            data = response.json()

            st.session_state.state = data.get("state", {})

            answer = data["response"]

            time.sleep(0.5)

        # typing animation
        placeholder = st.empty()
        text = ""

        for word in answer.split():
            text += word + " "
            time.sleep(0.02)
            placeholder.markdown(text + "▌")

        placeholder.markdown(text)

    st.session_state.history.append(("assistant", answer))