import streamlit as st
from widget.sidebar import sidebar

with st.sidebar:
    sidebar()

st.write(st.session_state["choice"])