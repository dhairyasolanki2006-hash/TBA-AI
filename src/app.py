import streamlit as st
from handler import handle_query

st.set_page_config(page_title="FRC AI Project 1", page_icon="🤖")
st.title("🤖 TBA AI ")

if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "...", "content": "..."}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask about a team, event, matches...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    response = handle_query(user_input)
    st.session_state.messages.append({"role": "assistant", "content": str(response)})
    st.rerun()