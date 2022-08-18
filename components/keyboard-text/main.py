import streamlit as st
from htbuilder import span


def load_key_css():
    st.write(
        """<style>
        .keyx {
        background-color: #eee;
        border-radius: 3px;
        border: 1px solid #b4b4b4;
        box-shadow: 0 1px 1px rgba(0, 0, 0, .2), 0 2px 0 0 rgba(255, 255, 255, .7) inset;
        color: #333;
        display: inline-block;
        font-size: .85em;
        font-weight: 700;
        line-height: 1;
        padding: 2px 4px;
        white-space: nowrap;
    }
    </style>""",
        unsafe_allow_html=True,
    )


def key(text: str, write: bool = True) -> str:
    """Applies a custom CSS to input text which makes it look like a keyboard key.
    To be used after running load_key_css() at least once in the app!

    Args:
        text (str): Text that will be styled as a key
        write (bool): If True, this will st.write() the key
    Returns:
        str: HTML of the text, styled as a key
    """

    key_html = str(span(_class="keyx")(text))

    if "loaded_key_css" not in st.session_state:
        load_key_css()
        st.session_state["loaded_key_css"] = True

    if write:
        st.write(key_html, unsafe_allow_html=True)

    return key_html


def example_default():
    key("⌘+K")


def example_inline():
    st.write(
        f"Also works inline! Example: {key('⌘+K', write=False)}",
        unsafe_allow_html=True,
    )
