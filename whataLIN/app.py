import streamlit as st
from widget import sidebar

with st.sidebar:
    sidebar.sidebar()

choice = st.session_state["choice"]

if choice == sidebar.OptionMenu.MAIN:
    widget.main_page.main_page()
