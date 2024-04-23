# Streamlit Chat Handler

Streamlit Chat Handler is a Python library designed to manage and render chat elements within a Streamlit application. This library simplifies the process of creating, storing, and dynamically rendering messages in a chat interface, supporting interactive communication scenarios in Streamlit.

## Features

- **Session Management**: Uses a singleton pattern to ensure a unique chat handler instance per session.
- **Dynamic Rendering**: Seamlessly append and render chat elements as user or assistant within the Streamlit session.
- **Customizable Chat Elements**: Supports different types of messages, such as text and markdown, with the flexibility to pass additional arguments and keyword arguments for rendering.

## Installation

You can install the `Streamlit Chat Handler` via pip:

```bash
pip install streamlit-chat-handler
```

## Quick Start

Here's a quick example to get started with using `Streamlit Chat Handler` in your Streamlit app:

```python
import uuid
from time import sleep
import streamlit as st
from streamlit_chat_handler import StreamlitChatHandler

# Initialize session
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

# Create a chat handler instance
chat_handler = StreamlitChatHandler(
    st.session_state,
    session_id=st.session_state["session_id"],
).render()

# Process user input
if prompt := st.chat_input("What is up?"):
    chat_handler.append(role="user", type="markdown", content=prompt, render=True)

    with st.spinner("Processing..."):
        sleep(1)
        chat_handler.append(role="assistant", type="markdown", content="answer", render=True)

```

## Documentation

### Class: StreamlitChatHandler

This class handles the state and rendering of chat elements within a Streamlit session. It is designed to manage chat elements dynamically, maintaining a unique instance per session through a singleton pattern.

#### Methods

- `append`: Adds a new chat element to the session.
- `render`: Renders all chat elements stored in the session.
- `render_last`: Renders the last added chat element.

### Class: StreamlitChatElement

Defines the structure of a chat element, handling its rendering through Streamlit's API.

#### Attributes

- `role`: Specifies whether the message is from a user or an assistant.
- `type`: Defines the Streamlit widget type for rendering (`text`, `markdown`, etc.).
- `content`: The content to be rendered, depends on the `type`.

#### Method

- `render`: Renders the chat element using the specified Streamlit widget.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests to contribute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
