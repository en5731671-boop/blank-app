import streamlit as st
from datetime import date

st.set_page_config(page_title="今日の脳みそチェック", layout="centered")

# --- 初期化（理解度3の連続カウント用） ---
if "understanding_streak" not in st.session_state:
    st.session_state.understanding_streak = 0

st.title("🧠 今日の脳みそチェック")
st.caption("※成績・単位・人生には一切影響ありません")

# --- 入力 ---
st.subheader("📚 今日の授業")
class_name = st.text_input(
    "正確じゃなくてOK",
    placeholder="例：たぶんデューイの話してた回"
)

st.subheader("🤔 正直チェックタイム")

understanding = st.radio(
    "理解度どうやった？",
    ("めっちゃわかった", "うっすらわかった", "正直わからん")
)

concentration = st.radio(
    "集中できとった？",
    ("脳みそフル稼働", "たまに宇宙行ってた", "ほぼ別の世界")
)

comment = st.text_area(
    "ひとことメモ（未来の自分へ）",
    placeholder="例：経験→ふり返り、また聞いた"
)

# --- 数値化 ---
u_score = {
    "めっちゃわかった": 3,
    "うっすらわかった": 2,
    "正直わからん": 1
}[understanding]

c_score = {
    "脳みそフル稼働": 3,
    "たまに宇宙行ってた": 2,
    "ほぼ別の世界": 1
}[concentration]

# --- 結果表示 ---
if st.button("📝 ふり返っとく"):
    st.subheader("📊 今日の結果")

    st.write(f"**授業メモ**：{class_name if class_name else '（記憶があいまい）'}")

    st.write("🧠 理解度：" + "🟩" * u_score + "⬜" * (3 - u_score))
    st.write("🎧 集中度：" + "🟦" * c_score + "⬜" * (3 - c_score))

    # --- 集中度ネタ ---
    if c_score == 1:
        st.warning("🧠 今日は脳みそ留守でした")

    # --- 理解度ストリーク管理 ---
    if u_score == 3:
        st.session_state.understanding_streak += 1
    else:
        st.session_state.understanding_streak = 0

    if st.session_state.understanding_streak >= 3:
        st.success("📈 成長しとるで（理解度3が連続中）")

    # --- コメント ---
    st.write("✏️ ひとことメモ")
    st.code(comment if comment else "（未来の自分、思い出せ）")
