import streamlit as st
import widget

with st.sidebar:
    widget.sidebar.sidebar()

choice = st.session_state["choice"]

if choice == widget.sidebar.OptionMenu.MAIN:
    widget.main_page.main_page()
