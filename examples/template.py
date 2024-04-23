import uuid
from time import sleep

import streamlit as st

from streamlit_chat_handler import StreamlitChatHandler


if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

print(type(st.session_state))

st.title("Template")

chat_handler = StreamlitChatHandler(
    st.session_state,
    session_id=st.session_state["session_id"],
).render()

if prompt := st.chat_input("Digite aqui..."):
    chat_handler.append(role="user", type="markdown", content=prompt, render=True)

    with st.spinner("Processando..."):
        sleep(1)
        chat_handler.append(
            role="assistant", type="markdown", content="resposta", render=True
        )
