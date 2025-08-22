import streamlit as st

# CSS 꾸미기
st.markdown("""
    <style>
    .product-card {
        background-color: #ffe6f0;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
    }
    .product-title {
        color: #ff4da6;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .section-title {
        color: #ff66b3;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 샘플 데이터베이스 (다양한 제품 추가)
cosmetics_db = {
    "라네즈 워터뱅크 크림": {
        "성분": ["정제수", "글리세린", "프로판다이올", "하이알루론산", "향료"],
        "효과": "피부 깊은 보습 및 수분 장벽 강화",
        "알러지 유발 가능 성분": ["향료"],
        "피부 타입 적합도": "건성, 복합성 피부에 적합",
        "주요 기능": ["보습", "장벽 강화"],
        "EWG 등급 요약": "대부분 성분은 1~2등급(안전), 일부 향료는 5등급(주의)"
    },
    "닥터자르트 시카페어 크림": {
        "성분": ["병풀추출물", "나이아신아마이드", "글리세린", "마데카소사이드", "에탄올"],
        "효과": "손상 피부 회복 및 진정 효과",
        "알러지 유발 가능 성분": ["에탄올"],
        "피부 타입 적합도": "민감성, 트러블 피부에 적합",
        "주요 기능": ["진정", "재생"],
        "EWG 등급 요약": "주요 성분은 1~2등급(안전), 에탄올은 3등급(주의)"
    },
    "이니스프리 그린티 씨드 세럼": {
        "성분": ["녹차추출물", "글리세린", "판테놀", "부틸렌글라이콜", "향료"],
        "효과": "피부 보습 및 항산화 효과",
        "알러지 유발 가능 성분": ["향료"],
        "피부 타입 적합도": "모든 피부 타입에 적합, 특히 건조 피부",
        "주요 기능": ["보습", "항산화"],
        "EWG 등급 요약": "대부분 성분은 1~2등급(안전), 일부 향료는 5등급(주의)"
    },
    "에뛰드 하우스 모이스트 풀 콜라겐 크림": {
        "성분": ["정제수", "글리세린", "콜라겐", "부틸렌글라이콜", "향료"],
        "효과": "피부 탄력 개선 및 보습",
        "알러지 유발 가능 성분": ["향료"],
        "피부 타입 적합도": "건성 피부에 적합",
        "주요 기능": ["보습", "탄력"],
        "EWG 등급 요약": "대부분 1~2등급, 일부 향료 5등급"
    },
    "클리오 킬커버 파운웨어 쿠션": {
        "성분": ["정제수", "티타늄디옥사이드", "징크옥사이드", "글리세린", "실리카"],
        "효과": "피부 톤 보정 및 자외선 차단",
        "알러지 유발 가능 성분": [],
        "피부 타입 적합도": "모든 피부 타입에 적합",
        "주요 기능": ["커버력", "자외선 차단"],
        "EWG 등급 요약": "대부분 성분 1~2등급"
    },
    "미샤 타임레볼루션 나이트 리페어 앰플": {
        "성분": ["정제수", "발효된 효모 추출물", "나이아신아마이드", "글리세린", "향료"],
        "효과": "피부 재생 및 보습 강화",
        "알러지 유발 가능 성분": ["향료"],
        "피부 타입 적합도": "모든 피부 타입, 특히 민감성 피부 주의",
        "주요 기능": ["재생", "보습", "항산화"],
        "EWG 등급 요약": "대부분 성분 1~2등급, 일부 향료 5등급"
    }
}

# 웹사이트 제목
st.title("💖 화학공학 × 화장품 성분 분석기 💖")
st.write("제품명을 입력하면 귀엽게 분석해드려요~ 🥰")

# 사용자 입력
product_name = st.text_input("제품명을 입력하세요:")

# 버튼 클릭 시 분석
if st.button("제품 분석하기"):
    if product_name in cosmetics_db:
        data = cosmetics_db[product_name]
        
        st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="product-title">💗 {product_name} 💗</div>', unsafe_allow_html=True)
        st.markdown(f'<p><span class="section-title">성분:</span> {", ".join(data["성분"])}</p>', unsafe_allow_html=True)
        st.markdown(f'<p><span class="section-title">효과:</span> {data["효과"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p><span class="section-title">알러지 유발 성분:</span> {", ".join(data["알러지 유발 가능 성분"])}</p>', unsafe_allow_html=True)
        st.markdown(f'<p><span class="section-title">피부 타입 적합도:</span> {data["피부 타입 적합도"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p><span class="section-title">주요 기능:</span> {", ".join(data["주요 기능"])}</p>', unsafe_allow_html=True)
        st.markdown(f'<p><span class="section-title">EWG 등급 요약:</span> {data["EWG 등급 요약"]}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.error("⚠️ 데이터베이스에 없는 제품입니다. 다른 제품명을 입력해보세요.")
