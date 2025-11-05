import streamlit as st
from chatbot import app
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(
    page_title="Revenue Analytics Agent",
    page_icon=":bar_chart:",
    layout="wide"
)

if 'message_history' not in st.session_state:
    st.session_state.message_history = [AIMessage(content='Hello I am the revenue analytics bot how can I help you today?')]

left_col, main_col = st.columns([1, 2])

with left_col:
    if st.button("Clear Conversation"):
        st.session_state.message_history = [{"role": "assistant", "content": "Ask me anything about revenue!"}]

with main_col:
    user_input = st.chat_input("Type here...")

    if user_input:
        st.session_state.message_history.append(
            HumanMessage(content=user_input)
        )
    response = app.invoke({"messages": st.session_state.message_history})

    st.session_state.message_history = response['messages']

    for message in reversed(st.session_state.message_history):
        if isinstance(message, HumanMessage):
            message_box = st.chat_message("user")
        else:
            message_box = st.chat_message("assistant")
        message_box.markdown(message.content)

