import streamlit as st
import time

st.write("진행 중입니다...")

progress = st.progress(0)

for i in range(101):
    time.sleep(0.03)  # 작업 시뮬레이션
    progress.progress(i)

st.success("완료되었습니다!")

