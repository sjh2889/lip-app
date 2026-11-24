import streamlit as st

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="맞춤형 립 추천기", page_icon="💄", layout="centered")

# 2. 제목 및 설명
st.title("💄 나이와 인종별 맞춤 립 추천기")
st.write("인종과 나이를 선택한 후 분석 버튼을 눌러보세요!")
st.divider()

# 3. 사용자 입력 받기
col1, col2 = st.columns(2)

with col1:
    race = st.selectbox(
        "인종을 선택하세요",
        ["Asian", "Black", "White", "Hispanic"]
    )

with col2:
    age = st.selectbox(
        "나이를 선택하세요",
        ["10~20대", "3~40대", "50~60대", "over70"]
    )

st.write("")  # 여백

# 4. 분석 버튼 및 조건별 결과 로직
if st.button("분석", use_container_width=True):
    st.divider()

    # 조건별 [컬러, 제형] 설정
    if race == "Asian":
        if age == "10~20대":
            color = "코랄 "
            texture = "글로시 틴트"
        elif age == "3~40대":
            color = "MLBB 말린 장미"
            texture = "벨벳 매트"
        elif age == "50~60대":
            color = "우아한 로즈 레드"
            texture = "촉촉한 새틴"
        else:  # over70
            color = "맑은 핑크 베리"
            texture = "고보습 립밤"

    elif race == "Black":
        if age == "10~20대":
            color = "초콜릿 브라운 누드"
            texture = "립글로스"
        elif age == "3~40대":
            color = "딥 플럼 버건디"
            texture = "리퀴드 매트"
        elif age == "50~60대":
            color = "리치 마호가니"
            texture = "크리미 새틴"
        else:  # over70
            color = "와인 베리"
            texture = "모이스처 립스틱"

    elif race == "White":
        if age == "10~20대":
            color = "피치 핑크"
            texture = "쉬어 글로스"
        elif age == "3~40대":
            color = "클래식 트루 레드"
            texture = "소프트 매트"
        elif age == "50~60대":
            color = "소프트 모브 로즈"
            texture = "새틴 립스틱"
        else:  # over70
            color = "내추럴 핑크"
            texture = "하이드레이팅 밤"

    else:  # Hispanic
        if age == "10~20대":
            color = "웜 피치 코랄"
            texture = "립 오일"
        elif age == "3~40대":
            color = "브릭"
            texture = "벨벳 크림"
        elif age == "50~60대":
            color = "딥 로즈우드"
            texture = "촉촉한 크림"
        else:  # over70
            color = "크림슨 레드"
            texture = "글로시 립스틱"

    # 5. 요청하신 형식대로 결과 화면 출력
    st.subheader(f"선택한 정보 : {race} / {age}")
    st.success(f"가장 추천하는 것은 **[{color}, {texture}]** 입니다!")
    st.markdown(f"### *{age} 인 지금의 당신은 언제나 아름답습니다.*")
