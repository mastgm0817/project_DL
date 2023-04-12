import streamlit as st
from streamlit_option_menu import option_menu
from enum import Enum

class OptionMenu(Enum):
    MAIN = "메인페이지"

def build():
    '''Option Menu를 통한 Sidebar 구현'''
    # https://github.com/victoryhb/streamlit-option-menu
    # -> 위 저장소를 통해 Option Menu Custom

    # 사이드바 메뉴
    args = [
        "Contents",
        [OptionMenu.MAIN.value, "장르 예측"] 
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
