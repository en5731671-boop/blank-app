import streamlit as st
import random

st.set_page_config(page_title="癒しアプリ", layout="centered")
st.title("🌿 今日の癒しアプリ")
st.caption("※今日のストレスを軽くして、ちょっと笑って終わるアプリです")

# --- 入力 ---
st.subheader("今日のストレス度を教えて")
stress = st.slider("1:超平和〜5:限界超え", 1, 5, 3)

st.subheader("今日の気分・状況を一言（任意）")
mood = st.text_input("例：仕事で疲れた、勉強しんどい…")

# --- 癒しアドバイス候補 ---
relax_tips = [
    "深呼吸して5秒キープ",
    "お気に入りの飲み物で一息",
    "ちょっと外に出て日光を浴びる",
    "軽くストレッチしてみる",
    "猫動画を見る（無敵）",
    "コーヒー片手に妄想タイム",
    "チョコひとかけで幸せ補充"
]

# --- ユーモアツッコミ ---
funny_comments = [
    "今日も脳みそ半休やな😂",
    "ストレス高め…アイスでごまかすしかないで！",
    "無理すんな、人生はラーメンの汁と同じやで",
    "大丈夫、猫は全部許してくれる",
    "ふーん、そういう日やな😏",
    "深呼吸より先に笑っとけ"
]

# --- 出力 ---
if st.button("🧘 癒しポイントを出す"):
    # ストレス度に応じてヒント数を変える
    tips_to_show = random.sample(relax_tips, k=min(stress, len(relax_tips)))
    st.subheader("🌟 今日の癒しポイント")
    for tip in tips_to_show:
        st.write(f"- {tip}")

    st.subheader("💬 今日のツッコミ")
    st.info(random.choice(funny_comments))

    if mood:
        st.subheader("📝 自分メモ")
        st.code(mood)

