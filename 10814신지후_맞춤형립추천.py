import streamlit as st

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="모두를 위한 립 추천기", page_icon="💄", layout="centered")

# 2. 리스트(List) 활용: 선택 옵션 및 강조 메시지 관리
race_list = ["Asian", "Black", "White", "Hispanic"]
age_list = ["10~20대", "3~40대", "50~60대", "over70"]
notice_list = [
    "💡 이 결과는 정답이 아닙니다."]

# 3. 함수(Function) + 조건문(if-elif-else) 활용: [컬러, 제형, 색상코드, 추천이유] 반환
def recommend_lip(selected_race, selected_age):
    if selected_race == "Asian":
        if selected_age == "10~20대":
            return ["코랄 핑크", "글로시 틴트", "#F26B7A", "노란 기가 감도는 피부에 형광등을 켜주며 생기 발랄한 분위기를 연출합니다."]
        elif selected_age == "3~40대":
            return ["MLBB 말린 장미", "벨벳 매트", "#B84A49", "차분하면서도 세련된 데일리 무드를 완성해 주는 자연스러운 로즈 컬러입니다."]
        elif selected_age == "50~60대":
            return ["우아한 로즈 레드", "촉촉한 새틴", "#C43E5C", "입술 주름 부각 없이 촉촉하게 혈색을 살려 얼굴을 화사하게 밝혀줍니다."]
        else:
            return ["맑은 핑크 베리", "고보습 립밤", "#D95D78", "건조하기 쉬운 입술에 깊은 보습과 은은한 생기를 동시에 더해줍니다."]

    elif selected_race == "Black":
        if selected_age == "10~20대":
            return ["초콜릿 브라운 누드", "립글로스", "#7B3F3B", "깊고 건강한 피부 톤과 자연스럽게 어우러지며 입술을 도톰하게 표현합니다."]
        elif selected_age == "3~40대":
            return ["딥 플럼 버건디", "리퀴드 매트", "#6B1D3A", "선명하고 깊이 있는 발색으로 카리스마 있고 고급스러운 매력을 극대화합니다."]
        elif selected_age == "50~60대":
            return ["리치 마호가니", "크리미 새틴", "#5C2626", "부드러운 윤기와 짙은 브라운 레드 빛이 우아하고 기품 있는 인상을 줍니다."]
        else:
            return ["와인 베리", "모이스처 립스틱", "#7A1C33", "깊이감 있는 와인 컬러가 입술에 입체감과 촉촉한 생기를 불어넣습니다."]

    elif selected_race == "White":
        if selected_age == "10~20대":
            return ["피치 핑크", "쉬어 글로스", "#F4979C", "맑고 밝은 피부 톤에 투명한 광택을 더해 풋풋하고 건강한 느낌을 살려줍니다."]
        elif selected_age == "3~40대":
            return ["클래식 트루 레드", "소프트 매트", "#C81D25", "하얀 피부와 선명한 대비를 이루어 이목구비를 더욱 또렷하게 만들어 줍니다."]
        elif selected_age == "50~60대":
            return ["소프트 모브 로즈", "새틴 립스틱", "#B56576", "피부가 창백해 보이지 않도록 차분하고 지적인 혈색을 자연스럽게 더해줍니다."]
        else:
            return ["내추럴 핑크", "하이드레이팅 밤", "#E07A8C", "가볍고 편안한 발림성으로 본연의 입술색처럼 자연스러운 생기를 줍니다."]

    else:  # Hispanic
        if selected_age == "10~20대":
            return ["웜 피치 코랄", "틴티드 립 오일", "#E56B6F", "따뜻하고 에너제틱한 올리브·태닝 피부 톤의 매력을 화사하게 돋보이게 합니다."]
        elif selected_age == "3~40대":
            return ["테라코타 브릭", "벨벳 크림", "#A44239", "구릿빛 피부 톤과 조화롭게 어우러지는 감각적이고 세련된 브릭 컬러입니다."]
        elif selected_age == "50~60대":
            return ["딥 로즈우드", "촉촉한 크림", "#8C3B3B", "부드럽고 고급스러운 로즈우드 빛이 성숙하고 우아한 분위기를 완성합니다."]
        else:
            return ["크림슨 레드", "글로시 립스틱", "#9E1B24", "화사하고 품격 있는 레드 컬러가 얼굴 전체에 활력과 생기를 불어넣습니다."]

# 4. 메인 화면 제목 및 기획 의도
st.title("💄 세상의 모든 아름다움을 위한 립 추천기")
st.info("🌍 **기획 의도:** 피부색과 나이에 상관없이, 세상의 모든 사람이 차별 없이 자신만의 고유한 아름다움을 찾길 바라는 마음으로 만들었습니다.")
st.divider()

# 5. 사용자 입력 받기 (리스트 사용)
col1, col2 = st.columns(2)
with col1:
    race = st.selectbox("🌍 인종을 선택하세요", race_list)
with col2:
    age = st.selectbox("🎂 나이를 선택하세요", age_list)

st.write("")

# 6. 분석 버튼 클릭 시 실행
if st.button("✨ 맞춤 립 분석하기", use_container_width=True, type="primary"):
    st.balloons()  # 축하 풍선 효과
    st.divider()
    
    # 함수 호출하여 결과 리스트 받아오기
    result = recommend_lip(race, age)
    color_name = result[0]
    texture = result[1]
    hex_code = result[2]
    reason = result[3]
    
    # 결과 헤더
    st.subheader(f"📌 선택한 정보 : {race} / {age}")
    
    # 실제 립 컬러 원형 미리보기 + 추천 결과 카드
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 24px; border-radius: 16px; border: 1px solid #e9ecef; border-left: 10px solid {hex_code}; margin-top: 10px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="width: 70px; height: 70px; border-radius: 50%; background-color: {hex_code}; box-shadow: 0 4px 10px rgba(0,0,0,0.15); flex-shrink: 0;"></div>
            <div>
                <p style="margin: 0; font-size: 18px; color: #212529;">
                    가장 추천하는 것은 <b style="color: {hex_code};">[{color_name}, {texture}]</b> 입니다!
                </p>
                <p style="margin: 8px 0 0 0; font-size: 14px; color: #495057;">
                    💡 {reason}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 다양성과 포용의 마지막 멘트
    st.markdown(f"### 💖 *{age}와 {race}에 상괸없이 당신은 있는 그대로 언제나 아름답습니다.*")
    st.divider()

    # 7. 반복문(for) 활용: "이 결과는 정답이 아닙니다" 메시지 반복 출력
    for msg in notice_list:
        st.warning(msg)
