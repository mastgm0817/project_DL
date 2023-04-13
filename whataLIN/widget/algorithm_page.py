import streamlit as st
import torch
import requests

def build():
    '''딥러닝 결과 출력 페이지 정의 및 구현'''
    st.subheader("딥러닝 페이지입니다.")
    show_pred()


def show_pred():

    get_image()
    st.write("어떤 알고리즘으로 예측해 볼까요?")

    option = ["SimpleCNN", "ResNet", "NfficientNet"]

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


