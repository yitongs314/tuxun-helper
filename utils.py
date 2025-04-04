import pandas as pd

def update_country_scores(df, question_label, user_answer, country_scores):
    matched_rows = df[(df["question"] == question_label) & (df["option"] == user_answer)]
    for _, row in matched_rows.iterrows():
        country = row["scoring_country"]
        score = row["score"]
        # 空值不计分
        if pd.notna(country) and pd.notna(score):
            country_scores[country] = country_scores.get(country, 0) + int(score)