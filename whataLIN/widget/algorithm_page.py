import streamlit as st
import torch
import requests
from PIL import Image

def build():
    '''딥러닝 결과 출력 페이지 정의 및 구현'''

    tab_labels = [
        "about Model", "Predict"
    ]
    tab0, tab1 = st.tabs(tab_labels)
   
    with tab0: model_tab() # 팀 소개
    with tab1: pred_tab() # 데이터 설명
    st.subheader("딥러닝 페이지입니다.")


def model_tab():
    option = ["구조", "손실"]
    op_img=st.selectbox("모델 정보", option)
    if op_img=="구조":
        url='whataLIN/structure.png'
    else:
        url='whataLIN/epoch-loss.png'
    image = Image.open(url)
    st.image(image, use_column_width=True)

def pred_tab():

    get_image()
    pred_button=st.button("예측")
    if pred_button:
        pred_genre()

def get_image():

    from PIL import Image
    uploaded_file = st.file_uploader("포스터 이미지 파일 업로드", type=['jpg', 'jpeg', 'png'])

    try: 
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='업로드된 이미지', use_column_width=True)
        else: st.write("이미지가 여기에 표시됩니다.")
    
    except:
        st.write(" ")

def pred_genre():
    pass


