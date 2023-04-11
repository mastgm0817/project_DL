import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():
    ### 사이드바
    # 사이드바 메뉴
    args = [
        "Contents",
        ["메인페이지", "데이터페이지", "장르 예측"] 
    ]
    # CSS 꾸미기
    styles = {
        "container":
            {"padding": "4!important", "background-color": "#fafafa"},
        "icon":
            {"color": "black", "font-size": "25px"}, 
        "nav-link":
            {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected":
            {"background-color": "#02ab21"},
    }
    # 키워드 옵션
    kwargs = {
        "icons": ['house', 'kanban', 'bi bi-robot'],
        "menu_icon": "app-indicator",
        "default_index": 0,
        "styles": styles,
    }
    # 구현
    # session_state를 통해 choice key로 데이터 연결
    st.session_state["choice"] = option_menu(
        *args, **kwargs)