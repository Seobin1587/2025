import streamlit as st

# 귀여운 제목
st.markdown("<h1 style='text-align: center; color: pink;'>🌸 화학 제품 성분 분석기 🐰✨</h1>", unsafe_allow_html=True)
st.write("궁금한 제품을 입력하면 귀엽게 알려드릴게요~ 💖")

# 데이터베이스 (예시 제품)
products = {
    "라네즈 워터뱅크 크림": {
        "성분": "히알루론산, 글리세린, 베타인",
        "효과": "피부 보습, 수분 공급, 피부 장벽 강화",
        "알러지 성분": "향료",
        "피부 타입 적합도": "모든 피부, 특히 건성 피부",
        "주요 기능 키워드": "💧수분, 🌿촉촉, 🛡장벽강화",
        "EWG 등급 요약": "대부분 1~2등급 (안전)"
    },
    "닥터자르트 시카페어 크림": {
        "성분": "센텔라 아시아티카, 마데카소사이드, 판테놀",
        "효과": "진정, 피부 재생, 붉은기 완화",
        "알러지 성분": "에센셜 오일",
        "피부 타입 적합도": "민감성 피부에 적합",
        "주요 기능 키워드": "🍃진정, 🌱재생, 💚민감피부케어",
        "EWG 등급 요약": "대부분 1~3등급"
    },
    "이니스프리 그린티 씨드 세럼": {
        "성분": "녹차 추출물, 히알루론산, 판테놀",
        "효과": "항산화, 보습, 피부 진정",
        "알러지 성분": "향료",
        "피부 타입 적합도": "복합성·지성 피부",
        "주요 기능 키워드": "🌿항산화, 💧수분, 🍃진정",
        "EWG 등급 요약": "대부분 1~2등급"
    }
}

# 입력창 (예시 안내 포함)
st.info("예시: 라네즈, 닥터자르트, 이니스프리")
product_name = st.text_input("제품명을 입력해주세요 ✨")

# 부분 일치 검색 (입력값이 제품명 안에 포함되어 있는지 확인)
matched_products = [name for name in products if product_name in name]

# 검색된 제품이 있는 경우
if matched_products:
    # 여러 개가 검색되면 선택창 띄우기
    if len(matched_products) > 1:
        selected_product = st.selectbox("여러 제품이 검색됐어요! 선택해주세요 🐥", matched_products)
    else:
        selected_product = matched_products[0]  # 하나면 바로 선택
    
    st.success(f"✨ '{selected_product}' 찾았어요! 보고 싶은 내용을 골라주세요 🎀")

    # 라디오 버튼으로 원하는 항목 선택
    option = st.radio(
        "무엇을 보고 싶나요? 💖",
        ("성분", "효과", "알러지 성분", "피부 타입 적합도", "주요 기능 키워드", "EWG 등급 요약")
    )

    # 귀여운 카드 스타일 출력
    st.markdown(
        f"""
        <div style="background-color:#fff0f6; padding:15px; border-radius:20px; 
        box-shadow: 2px 2px 10px #ffb6c1; margin:10px;">
        <h3 style="color:#ff69b4;">🌸 {option} 🌸</h3>
        <p style="font-size:18px;">{products[selected_product][option]}</p>
        </div>
        """, unsafe_allow_html=True
    )

# 입력했지만 결과가 없는 경우
elif product_name:
    st.error("😢 죄송해요, 아직 데이터에 없는 제품이에요!")
