import streamlit as st
import plotly.express as px
import pandas as pd
import ui
import utils
from sun_tutorial import show_sun_direction_expander

st.set_page_config(page_title="GeoTrainer 辅助模式", layout="centered")

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

# 加载题库数据
df_vehicle = pd.read_csv("data/vehicle.csv")
df_sun_position = pd.read_csv("data/sun_position.csv")
df_language = pd.read_csv("data/language.csv")
df_excluded_country = pd.read_csv("data/excluded_country.csv")

question_bank = {
    "车牌": df_vehicle,
    "太阳方位": df_sun_position,
    "语言": df_language
}

keywords = list(question_bank.keys())
selected_keywords = st.multiselect("你看到哪些街景信息？", keywords, default=keywords)

# 初始化排除国家
excluded_countries = set()
# 初始化得分
country_scores = {}
answers = {}

# 左侧sidebar
with st.sidebar:
    for keyword in selected_keywords:
        df = question_bank[keyword]
        questions = df["question"].unique().tolist()
        for i, q in enumerate(questions):
            #subset = df[df["question"]==q]
            user_answer = ui.render_image_radio(df, q, i)
            answers[q] = user_answer
            if keyword == "太阳方位": # and q["label"] == "太阳偏北还是偏南？":
                show_sun_direction_expander()
            if not user_answer:
                continue

            # 更新 excluded_countries
            exclusion = df_excluded_country[
                (df_excluded_country["question"] == q) & 
                (df_excluded_country["option"] == user_answer)
            ]
            exclusion_list = exclusion["excluded_country"].unique().tolist()
            for c in exclusion_list:
                excluded_countries.update(c)

            # 计分
            utils.update_country_scores(df, q, user_answer, country_scores)
            

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