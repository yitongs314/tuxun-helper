import streamlit as st
import pandas as pd

def chunk_list(lst, n):
    # 将列表每 n 项分为一组
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def render_image_radio(df, question_text, q_index):
    """
    渲染一个带图片的单选题（支持CSV结构）
    
    参数：
    - df: 当前keyword对应的DataFrame
    - question_text: 具体问题文本
    - q_index: 当前是第几个问题（防止Streamlit控件冲突）
    """
    st.subheader(f"{question_text}")

    # 取出当前问题对应的所有选项
    subset_df = df[df["question"] == question_text]

    labels = subset_df["option"].unique().tolist()
    image_map = dict(zip(subset_df["option"].unique(), subset_df["image"].unique()))

    max_per_row = 3  # 每行最多显示几个
    rows = chunk_list(labels, max_per_row)

    for row in rows:
        cols = st.columns(len(row))
        for i, label in enumerate(row):
            with cols[i]:
                img_path = image_map.get(label)
                if pd.notna(img_path) and img_path.strip() != "":
                    st.image(f"{img_path}", use_container_width=True)
                st.write(label)

    selected = st.radio("请选择一个选项：", labels, key=f"{question_text}_{q_index}_radio")
    return selected