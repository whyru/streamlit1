import streamlit as st

'''
텍스트 요소
'''
# 제목 및 섹션 구분
st.title("앱의 제목을 표시하기") # 앱의 메인 제목 표시
st.header("작은 제목이나 섹션 구분") # 섹션의 주요 제목
st.subheader("섹션 하위 구분") # 하위 섹션의 제목
# 다양한 출력 형식
st.write("텍스트를 포함하여 다양한 형식의 데이터를 출력합니다.") # 일반 텍스트 및 데이터를 출력
st.text("설명이나 추가 정보같은 일반 텍스트 출력하기") # 설명을 위한 단순 텍스트 출력
st.code("print('Hello, teachers!')") # 코드 블록 형태로 출력
# 메시지 알림 및 강조
st.error("오류창을 나타내거나 빨간 상자로 강조하기")
st.success("실행완료창을 나타내거나 초록 상자로 강조하기")
st.info("간단한 정보를 안내하거나 파란색 상자로 강조하기")
st.warning("경고창을 띄우거나 노란색 상자로 강조하기")

'''
인풋 요소 ➊ 인풋 요소 종류
'''
# 버튼 클릭 이벤트 처리
if st.button("클릭해보세요!!"): # 버튼을 클릭하면 아래 메시지 출력
    st.write("버튼을 누르셨군요. 잘하셨습니다!")
# 닉네임 입력 받기
name = st.text_input("닉네임을 입력해주세요.") # 텍스트 입력 상자에서 닉네임 입력
if name: # 닉네임이 입력된 경우에만 아래의 메시지 출력
    st.write(name + "님 안녕하세요! 반갑습니다.")
# 슬라이더로 숫자 선택
number = st.slider("책을 읽은지 며칠째인가요?", 0, 100) # 0부터 100 사이의 숫자 선택
st.write(number, "일째이군요!") # 선택한 숫자를 출력

'''
인풋 요소 ➋ 조건문과 함께 사용하기
'''
# 자연수 입력 받기
number = st.number_input('자연수를 입력해주세요.', min_value=0, step=1, value=None)
# 홀수/짝수 판별
if number is None:
    st.info('아직 자연수를 입력하지 않으셨습니다.')
else:
    if number % 2 == 1: # 홀수 조건
        st.info('입력하신 자연수는 홀수입니다.')
    else: # 짝수 조건
        st.info('입력하신 자연수는 짝수입니다.')

'''
미디어 요소
'''
# 이미지 표시
st.subheader("이미지 표시")
st.image("media/sample_image.png", caption="여기에 그림 설명을 입력할 수 있습니다. ")
st.subheader("영상 표시") 
st.video("media/sample_video.mp4") # 영상 표시
st.subheader("음악 재생")
st.audio("media/sample_music.mp3") # 음악 재생

'''
레이아웃과 컨테이너
'''
# 확장 레이아웃
with st.expander("자세히 보기"):
    st.write("이 레이아웃에 대한 자세한 내용입니다.") # 확장 레이아웃 내용

# 두 개의 열 생성
col1, col2 = st.columns(2)
with col1:
    st.subheader("첫 번째 열입니다.") # 첫 번째 열 내용
    st.write("첫 번째 열에 대한 내용을 입력하세요.")
with col2:
    st.subheader("두 번째 열입니다.") # 두 번째 열 내용
    st.write("두 번째 열에 대한 내용을 입력하세요.")

'''
데이터와 차트 요소
'''
import pandas as pd
import numpy as np

# 50개의 난수를 가지는 데이터프레임 생성
data = pd.DataFrame({
    'A': np.random.randn(50),
    'B': np.random.randn(50)
})

st.write(data) # 데이터 프레임 출력
st.line_chart(data) # 라인 차트 출력
st.bar_chart(data) # 바 차트 출력
