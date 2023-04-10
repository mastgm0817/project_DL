import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import joblib
import xgboost as xgb
import seaborn as sns
from streamlit_option_menu import option_menu


with st.sidebar:
    choice = option_menu("Contents", ["메인페이지", "데이터페이지", "장르 예측"],
                         icons=['house', 'kanban', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choice == "메인페이지":

    tab0, tab1, tab2, tab3 = st.tabs(["🏠 Main", "🔎Explain", "🗃 Data", "🖇️ Link"])
   

    with tab0:
        tab0.subheader("딥러닝프로젝트")            # 팀이름 정해야댐
        st.write()
        '''
        **⬆️위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다!⬆️**

        ---

        ### Team 💪

        | 이름 | 역할 분담 | 그 외 역할 | GitHub |
        | :---: | :---: | :---: | :---: |
        | 고병연 | 딥러닝 |  | [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/whataLIN)|
        | 박상원 | 딥러닝 |  | [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)]|
        | 이규린 | streamlit 제작 |  | [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)]|
    
        ---
        
        '''
    with tab1:
        tab1.subheader("🔎Explain")
        tab1.write()
        '''
        ### 자료 설명
        > * 
        > * 

        '''
    with tab2:
        tab2.subheader("🗃 Data Tab")
        st.write("다음은 CSV 데이터의 일부입니다.")
        # GitHub URL
        url = "" #링크 추가

        # CSV 파일 읽기
        try:
            df = pd.read_csv(url)
        except pd.errors.EmptyDataError:
            st.error("CSV 파일을 찾을 수 없습니다.")
            st.stop()
        # DataFrame 출력
        st.write(df)
        tab2.write()
        '''
        ###### 각 Columns의 설명입니다.
        > * ㅁㄴㅇㄹ

        '''

    with tab3:
        tab3.subheader("🖇️ Link Tab")
        tab3.write("추가적인 자료는 아래의 링크에서 확인 하시면 됩니다.")
        st.write()
        '''

        | 구분 | 이름  | 링크 | 
        | :---: | :---: | :---: | 
        | Kaggle | | [![Colab](https://img.shields.io/badge/kaggle-College%20Basketball%20Dataset-skyblue)][https://www.kaggle.com/datasets/raman77768/movie-classifier/code] | 
        | Notion |  | [![Notion](https://img.shields.io/badge/Notion-Sports%20TooToo-lightgrey)][https://www.notion.so/925e2766791248a58cd3bf7623fbb90a] | 
        | Colab | 🤖전처리 데이터 | [![Colab](https://img.shields.io/badge/colab-Data%20preprocessing-yellow)] | 
        
        '''

elif choice == "데이터페이지":
    tab0, tab1 = st.tabs(["🗃 Data", "📈 Chart"])
    data = np.random.randn(10, 1)
    with tab0:
        tab0.subheader("🗃 Data Tab")
        st.write("사용된 전체 csv파일")
        url = ""        #링크 추가
        df = pd.read_csv(url)
        st.write(df)

        options = st.selectbox(
                '검색하고 싶은 데이터를 골라주세요',
                ('Index', 'Columns', 'Index_in_Column'))
        if options == 'Index':
            index_name = st.text_input('검색하고 싶은 index를 입력해 주세요')
            filtered_df = df[df.apply(lambda row: index_name.lower() in row.astype(str).str.lower().values.tolist(), axis=1)]
            st.write(filtered_df)


        elif options == 'Columns':
            column_name = st.text_input('검색하고 싶은 columns를 입력해 주세요')
            if column_name in df.columns:
                filtered_df = df[[column_name]]
                st.write(filtered_df)
            else:
                st.write('Column이 입력되지 않았습니다.')

        
        elif options == 'Index_in_Column':
            column_names = st.text_input('검색하고 싶은 Columns를 입력하세요')
            # 입력한 컬럼명이 존재하는 경우
            if column_names in df.columns:
                c_index = st.text_input('그 Columns내에 있는 검색하고 싶은 Index를 입력하세요 ')
                # 입력한 점수와 일치하는 행 찾기
                if c_index.isdigit():
                    c_index = int(c_index)
                    filtered_df = df[(df[column_names] == c_index)]
                # 검색 결과 출력하기
                    if not filtered_df.empty:
                        st.write(filtered_df)
                    else:
                        st.write('검색된 Index가 없습니다.')
                else:
                    filtered_df = df[(df[column_names] == c_index)]
                    st.write(filtered_df)
            else:
                st.write('검색된 Columns가 없습니다.')
            
            
        st.write("")


elif choice == "장르 예측":
    pass