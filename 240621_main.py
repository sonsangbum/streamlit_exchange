# 실행은 터미널에서 streamlit run 240621_main.py
#https://github.com/ 에서 URL생성
#https://streamlit.io/ 에 파일업데이트 

import streamlit as st
from PIL import Image   #이미지를 불러올때 사용
import exchange_rate_240619

# st.title("안녕하세요!")
# st.header("손상범")

#사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value="",max_chars=15)
user_password = st.sidebar.text_input("패스워드 입력", value="",type="password")

if user_id=='ssb2001' and user_password == "1234" :
        
    st.sidebar.header("그림 목록")
    # sel_options=["","진주 귀걸이를 한 소녀","별이 빛난는 밤","절규","생명의 나무","월하정인"] #셀렉트 박스
    # user_opt = st.sidebar.selectbox('좋아하는 작품은? ', sel_options, index=0)
    # st.sidebar.write("***선택한 그림은 ", user_opt)

    menu= st.sidebar.radio("메뉴 선택",['환율 조회','부동산 조회(EDA)','인공지능 예측/분류'],index=None)
    
    # if menu== '환율 조회':
    #     st.sidebar.write("환율 조회")
    # elif menu== '부동산 조회(EDA)':
    #     st.sidebar.write("부동산 조회(EDA)")
    # elif menu== '인공지능 예측/분류':
    #     st.sidebar.write("인공지능 예측/분류")
    # else :
    #     st.sidebar.write("메뉴 선택해주세요")

    if menu == '환율 조회':
        exchange_rate_240619.exchange_main()
        st.sidebar.write("환율 조회")
    elif menu== '부동산 조회(EDA)':
        st.sidebar.write("부동산 조회(EDA)")
    elif menu== '인공지능 예측/분류':
        st.sidebar.write("인공지능 예측/분류")
    else :
        st.sidebar.write("메뉴 선택해주세요")

    #메인 화면(오른쪽 화면)
    # st.subheader(user_opt,divider='rainbow')


