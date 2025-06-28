import streamlit as st
import json

# JSON 파일 불러오기
with open("obgyn_diagnosis_explanations.json", "r", encoding="utf-8") as f:
    diagnosis_data = json.load(f)

st.title("AI 산부인과 진단 설명기")

# 진단명 선택
selected = st.selectbox("진단명을 선택하세요:", list(diagnosis_data.keys()))

# 설명 표시
if selected:
    st.subheader(selected)
    st.write(diagnosis_data[selected])