import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def get_table():
    df_url = "https://github.com/whataLIN/project_DL/raw/main/whataLIN/df.csv" 
    return pd.read_csv(df_url)

def build():
    '''메인페이지 하부 탭 정의 및 구현'''

    # 탭 정의
    tab_labels = [
        "🏠 Main", "🔎Explain", "🗃 Data", "🖇️ Link"
    ]
    tab0, tab1, tab2, tab3 = st.tabs(tab_labels)
   
    with tab0: intro_tab() # 팀 소개
    with tab1: explain_tab() # 데이터 설명
    with tab2: data_tab() # 
    with tab3:
        tab3.subheader("🖇️ Link Tab")
        tab3.write("추가적인 자료는 아래의 링크에서 확인 하시면 됩니다.")
        st.write()
        '''

        | 구분 | 이름  | 링크 | 
        | :---: | :---: | :---: | 
        | Kaggle | movie poster | [![Colab](https://img.shields.io/badge/kaggle-College%20Basketball%20Dataset-skyblue)][https://www.kaggle.com/datasets/raman77768/movie-classifier/code] | 
        | Notion | 딥러닝 프로젝트 | [![Notion](https://img.shields.io/badge/Notion-Sports%20TooToo-lightgrey)][https://www.notion.so/925e2766791248a58cd3bf7623fbb90a] | 
        | Colab | 🤖전처리 데이터 | [![Colab](https://img.shields.io/badge/colab-Data%20preprocessing-yellow)] | 
        
        '''

def intro_tab():
    '''팀원 소개 및 역할 분담'''

    # TODO : 팀이름 정해야댐
    team_name = "딥러닝프로젝트"
    st.subheader(team_name)
    st.write('**⬆️위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다!⬆️**')
    st.write('---')
    st.subheader('Team 💪')
    st.write(
        '''
        | 이름 | 역할 분담 | GitHub |
        | :---: | :---: | :---: |
        | 고병연 | efficientNet, CNN | [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/whataLIN)|
        | 박상원 | 시각화 |  [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)]|
        | 이규린 | ResNet, streamlit 구현 |  [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)]|
        '''
    )
    st.write('---')

def explain_tab():
    st.subheader("🔎Explain")

    # 표 데이터 로딩
    try:
        df = get_table()
    except pd.errors.EmptyDataError:
        st.error("CSV 파일을 찾을 수 없습니다.")
        st.stop()

    # 자료 설명 마크다운
    st.subheader("자료 설명")
    st.write(
        '''
        > * id : 영화 포스터에 부여된 ID
        > *	poster : 포스터 링크
        > * title : 영화 이름
        > * year : 개봉 연도
        > * rating : 별점
        > * genre : 영화의 장르. string 형태로 하나 이상의 장르가 묶인 형태
        > * 그 외 장르 이름을 열 이름으로 가지는 열은 영화의 장르를 One-Hot Encoding 방식으로 나타낸 것.
        '''
    )

    # 파이 차트 표시
    labels = ['action', 'adventure', 'animmation', 'comedy', 'crime', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 'short', 'thriler']
    values = [424, 238, 242, 667, 292, 829, 166, 354, 195, 342, 162, 201, 431]
    pie_chart(labels, values, title_text='Movie genre')

def pie_chart(labels, values, title_text=""):
    '''원형 plotly 차트'''
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title_text=title_text)
    st.plotly_chart(fig)

def data_tab():
    '''데이터 탭 구현'''

    st.subheader("🗃 Data Tab")
    st.write("다음은 CSV 데이터의 일부입니다.")
    # GitHub URL
    # CSV 파일 읽기
    try:
        df = get_table()
    except pd.errors.EmptyDataError:
        st.error("CSV 파일을 찾을 수 없습니다.")
        st.stop()
    # DataFrame 출력
    # st.table(df)
    # st.dataframe(df)
    st.subheader('각 Columns의 설명입니다.')
    st.write(
        '''
        > * 
        ''')