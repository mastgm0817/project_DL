import streamlit as st
from widget import sidebar, algorithm_page, main_page

with st.sidebar:
    sidebar.build()

choice = st.session_state["choice"]

if choice == sidebar.OptionMenu.MAIN.value:
    main_page.build()

if choice == sidebar.OptionMenu.Algorithm.value:
    algorithm_page.build()
