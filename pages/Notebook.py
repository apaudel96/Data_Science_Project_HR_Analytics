from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Notebook")


@st.cache
def get_html_string():
    html_path = Path(__file__).parent.parent / "notebook.html"

    html_string = html_path.read_text()
    return html_string


components.html(get_html_string(), height=800, scrolling=True)
