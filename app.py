import streamlit as st
import json

# JSON 파일 불러오기 (캐시 없이 자동 반영되도록 설정)
def load_json():
    with open("obgyn_diagnosis_explanations.json", "r", encoding="utf-8") as f:
        return json.load(f)

# JSON 불러오기
explanations = load_json()

# 제목
st.title("OBGYN Diagnosis Explanation App")

# 진단명 선택
diagnosis_list = sorted(explanations.keys())
selected_diagnosis = st.selectbox("🔎 진단명을 선택하거나 입력하세요", diagnosis_list)

# 설명 출력
if selected_diagnosis:
    st.subheader("📋 환자용 설명 (영어)")
    st.write(explanations[selected_diagnosis])

# 면책조항 (탭이 번거롭다면 그냥 하단 표시)
st.markdown("---")
st.markdown(
    "🔔 **Disclaimer:** This explanation is provided for general understanding only. "
    "Please consult your medical team for a diagnosis or treatment plan."
)
