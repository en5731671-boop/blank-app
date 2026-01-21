import streamlit as st
from datetime import date

# ページ設定
st.set_page_config(page_title="授業ふり返りチェック", layout="centered")

st.title("📘 授業ふり返りチェックアプリ")
st.write("授業後30秒で、理解度と集中度をふり返りましょう。")

# --- 入力フォーム ---
st.subheader("📝 今日の授業")

class_name = st.text_input("授業名を入力してください", placeholder="例：教育方法論 第10回")
today = st.date_input("日付", value=date.today())

st.subheader("📊 自己チェック")

understanding = st.radio(
    "理解度はどのくらいでしたか？",
    ("よく理解できた", "まあまあ理解できた", "あまり理解できなかった")
)

concentration = st.radio(
    "集中度はどのくらいでしたか？",
    ("集中できた", "少し気が散った", "ほとんど集中できなかった")
)

comment = st.text_area(
    "ひとことふり返り（今日わかったこと・次に意識したいこと）",
    placeholder="例：経験学習は実践とふり返りが重要だと理解できた"
)

# --- 数値化 ---
understanding_score = {
    "よく理解できた": 3,
    "まあまあ理解できた": 2,
    "あまり理解できなかった": 1
}[understanding]

concentration_score = {
    "集中できた": 3,
    "少し気が散った": 2,
    "ほとんど集中できなかった": 1
}[concentration]

# --- 送信 ---
if st.button("✅ ふり返りを保存・表示"):
    st.success("ふり返りを記録しました！")

    st.subheader("📌 今日のふり返り結果")

    st.write(f"**授業名**：{class_name}")
    st.write(f"**日付**：{today}")

    st.write("**理解度**：" + "★" * understanding_score + "☆" * (3 - understanding_score))
    st.write("**集中度**：" + "★" * concentration_score + "☆" * (3 - concentration_score))

    st.write("**コメント**")
    st.info(comment if comment else "（コメントなし）")
