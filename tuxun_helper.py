import streamlit as st
import plotly.express as px
import pandas as pd
import json
from sun_tutorial import show_sun_direction_expander

st.set_page_config(page_title="GeoTrainer 辅助模式", layout="centered")

def chunk_list(lst, n):
    """将列表每 n 项分为一组"""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def render_image_radio(question_data, keyword, q_index):
    st.subheader(f"{question_data['label']}")
    options = question_data["options"]

    labels = []
    image_map = {}

    for opt in options:
        label = opt["option_name"]
        labels.append(label)
        image_map[label] = opt.get("image", None)

    # ---------- 分多行展示 ----------
    max_per_row = 3  # 每行最多几个选项
    rows = chunk_list(labels, max_per_row)

    for row in rows:
        cols = st.columns(len(row))
        for i, label in enumerate(row):
            with cols[i]:
                if image_map[label]:
                    st.image(image_map[label], width=120)
                st.write(label)

    # ---------- 统一选择 ----------
    selected = st.radio("请选择一个选项：", labels, key=f"{keyword}_{q_index}_radio")
    return selected

def update_country_scores(score_dict, scoring_table, user_choice):
    if user_choice in scoring_table:
        for country, score in scoring_table[user_choice].items():
            score_dict[country] = score_dict.get(country, 0) + score
    return score_dict

st.markdown("# 🌍 图寻街景训练助手")
st.markdown("""
### 一款为图寻新手玩家量身定制的街景推理辅助工具！  
你可以在单机练习或娱乐对局中使用本工具～  
通过输入你在街景中观察到的**语言、车牌、电线杆、建筑风格等细节**，本工具将帮助你：  
✅ 自动排除不符合的国家/地区  
✅ 标记最可能的国家/地区  
### 使用须知：  
⚠️街景识别助手提供的答案仅供参考，实际答案请以游戏为准  
⚠️目前本工具仅包括“西湖十景”题库中的国家/地区  
⚠️**请勿在积分匹配中使用**  
""")


st.markdown("### 请选择你看到的街景要素")

# 加载题库
with open("questions.json", "r", encoding="utf-8") as f:
    question_bank = json.load(f)

keywords = list(question_bank.keys())
selected_keywords = st.multiselect("你看到哪些街景信息？", keywords, default=keywords)

# 初始化排除国家dictionary
excluded_countries = set()
# 初始化得分
country_scores = {}
answers = {}
with st.sidebar:
    for keyword in selected_keywords:
        topic = question_bank[keyword]
        questions = topic["questions"]

        for idx, q in enumerate(questions):
            user_choice = render_image_radio(q, keyword, idx)
            answers[q["label"]] = user_choice
            if keyword == "太阳方位" and q["label"] == "太阳偏北还是偏南？":
                show_sun_direction_expander()
            if not user_choice:
                continue

            # 检查是否有要排除的国家
            for opt in q["options"]:
                if opt["option_name"] == user_choice and "exclude" in opt:
                    excluded_countries.update(opt["exclude"])

            # 计分（排除掉不该出现的国家）
            scoring_table = q.get("scoring", {})
            if user_choice in scoring_table:
                for country, score in scoring_table[user_choice].items():
                    if country not in excluded_countries:
                        country_scores[country] = country_scores.get(country, 0) + score

# 将被排除的国家设为0（地图上没有颜色）
for country in excluded_countries:
    country_scores[country] = 0

# ---------- 地图展示 ----------
st.markdown("---")
st.markdown("### 📍 推测国家匹配度")

score_df = pd.DataFrame({
    "country": list(country_scores.keys()),
    "score": list(country_scores.values())
})

fig = px.choropleth(
    score_df,
    locations="country",
    locationmode="country names",
    color="score",
    color_continuous_scale="Blues"
)

st.markdown("当前选择总结")
if answers:
    for q, ans in answers.items():
        if answers:
            st.markdown(f"- **{q}**：{ans}")
        else:
            st.markdown("你还没有选择任何线索。")
st.markdown("---")

st.plotly_chart(fig, use_container_width=True)

with st.expander("📘 如何理解地图颜色？"):
    st.markdown("""
    - 深蓝色：高可能性  
    - 中蓝色：中可能性  
    - 浅蓝色：低可能性  
    - 灰色：被排除
    """)

with st.expander("❌ 查看已排除国家/地区列表"):
    st.markdown(", ".join(sorted(excluded_countries)))
