import streamlit as st
import pandas as pd


food_lists_by_range = {
    "low": [
        {"추천 식품": "삶은 달걀", "100g당 단백질": "13g", "추천 정도": "매우 추천 ★★★"},
        {"추천 식품": "그릭 요거트", "100g당 단백질": "10g", "추천 정도": "추천 ★★☆"},
        {"추천 식품": "두부", "100g당 단백질": "8g", "추천 정도": "보통 ★☆☆"},
    ],
    "medium": [
        {"추천 식품": "닭가슴살", "100g당 단백질": "23g", "추천 정도": "매우 추천 ★★★"},
        {"추천 식품": "연어", "100g당 단백질": "20g", "추천 정도": "추천 ★★☆"},
        {"추천 식품": "렌틸콩", "100g당 단백질": "9g", "추천 정도": "보통 ★☆☆"},
    ],
    "high": [
        {"추천 식품": "소고기 우둔살", "100g당 단백질": "22g", "추천 정도": "매우 추천 ★★★"},
        {"추천 식품": "닭가슴살", "100g당 단백질": "23g", "추천 정도": "매우 추천 ★★★"},
        {"추천 식품": "참치(살코기)", "100g당 단백질": "25g", "추천 정도": "추천 ★★☆"},
    ],
}


def get_protein_guide(weight):
    if weight < 60:
        recommended_protein = round(weight * 1.0)
        selected_foods = food_lists_by_range["low"]
        recommendation_level = "가벼운 활동 및 기초 유지 구간"
    elif 60 <= weight < 80:
        recommended_protein = round(weight * 1.2)
        selected_foods = food_lists_by_range["medium"]
        recommendation_level = "표준 체중 및 일반 활동 구간"
    else:
        recommended_protein = round(weight * 1.4)
        selected_foods = food_lists_by_range["high"]
        recommendation_level = "고중량 및 근력 유지 집중 구간"

    return recommended_protein, selected_foods, recommendation_level


def create_table_data(food_list):
    table_rows = []
    for item in food_list:
        table_rows.append({
            "추천 식품": item["추천 식품"],
            "100g당 단백질": item["100g당 단백질"],
            "추천 정도": item["추천 정도"],
        })
    return pd.DataFrame(table_rows)


st.title("단백질 섭취량 및 추천 식품 가이드")


weight = st.number_input("몸무게 입력: (kg)", min_value=1.0, max_value=300.0, value=65.0, step=0.1)

if st.button("분석하기"):
   
    protein_amount, foods, level_desc = get_protein_guide(weight)

    
    st.subheader(f"적정 단백질 섭취량은 {protein_amount}g입니다.")
    st.caption(f"적용 구간: {level_desc}")

    
    table_df = create_table_data(foods)
    st.table(table_df)
