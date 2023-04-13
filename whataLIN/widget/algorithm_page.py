import streamlit
import torch

st.write("딥러닝 페이지입니다.")
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
            poster = Image.open(uploaded_file)
            st.poster(poster, caption='업로드된 이미지', use_column_width=True)
            # img_size = image.size
            # st.write(f'이미지 크기: {img_size[0]}x{img_size[1]}')
            return poster
        else: st.write("이미지가 여기에 표시됩니다.")
    
    except:
        st.write(" ")