import uuid
from time import sleep

import streamlit as st

from streamlit_chat_handler import StreamlitChatHandler


if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

st.title("Template")

chat_handler = StreamlitChatHandler(
    st.session_state,
    session_id=st.session_state["session_id"],
).render()

if prompt := st.chat_input("Digite aqui..."):
    chat_handler.append(role="user", type="markdown", content=prompt, render=True)

    with st.spinner("Processando..."):
        sleep(1)


        container = "expander" if chat_handler.step_counter % 2 == 0 else "popover"
        cont_kwargs = {"label": "Teste",  "expanded": True} if chat_handler.step_counter % 2 == 0 else {"label": "Teste"}

        chat_handler.append(
            role="assistant",
            type="markdown",
            content=f'{chat_handler.step_counter} - resposta',
            parent=container,
            parent_kwargs=cont_kwargs,
            render=True,
        )

        chat_handler.append(
            role="assistant",
            type="markdown",
            content=f'{chat_handler.step_counter} - resposta',
            parent= "expander",
            parent_kwargs={"label": "Elemento renderizado a posteriori",  "expanded": True},
        )