import streamlit as st
import random
import pandas as pd
from datetime import date
import os

st.set_page_config(page_title="癒しアプリ（保存版）", layout="centered")
st.title("🌿 今日の癒しアプリ")
st.caption("ストレスを可視化＆癒しポイントを記録しつつ、ちょっと笑えるアプリ")

# --- CSV保存設定 ---
csv_file = "healing_log.csv"

# --- 初期化 ---
if "logs" not in st.session_state:
    if os.path.exists(csv_file):
        st.session_state.logs = pd.read_csv(csv_file)
    else:
        st.session_state.logs = pd.DataFrame(columns=["日付", "ストレス度", "癒しポイント", "ツッコミ", "メモ"])

# --- 入力 ---
st.subheader("今日のストレス度を教えて")
stress = st.slider("1:超平和〜5:限界超え", 1.0, 5.0, 3.0, 0.1)

st.subheader("今日の気分・状況を一言（任意）")
mood = st.text_input("例：仕事で疲れた、勉強しんどい…")

# --- レパートリー ---
relax_tips = [
    "深呼吸して5秒キープ", "お気に入りの飲み物で一息",
    "ちょっと外に出て日光を浴びる", "軽くストレッチしてみる",
    "猫動画を見る（無敵）", "コーヒー片手に妄想タイム",
    "チョコひとかけで幸せ補充", "スマホ置いて目を閉じる",
    "お気に入りの曲を1曲聴く", "手をもみもみしてリラックス",
    "深呼吸しながら変顔してみる", "ラーメン食べる妄想する",
    "お風呂で1分間瞑想", "今日1つラッキーなこと思い出す",
    "空を眺めて1分ぼーっとする", "ストレスを紙に書いて破る",
    "軽く腕立て10回", "好きな香りで深呼吸", "窓を開けて新鮮な空気吸う"
] * 3

funny_comments = [
    "今日も脳みそ半休やな😂", "ストレス高め…アイスでごまかすしかないで！",
    "無理すんな、人生はラーメンの汁と同じやで", "大丈夫、猫は全部許してくれる",
    "ふーん、そういう日やな😏", "深呼吸より先に笑っとけ",
    "今日は寝落ち推奨やで", "脳みそは有給休暇中です", 
    "コーヒーを求めて彷徨う日やな", "やる気スイッチは押さなくてOK",
    "ストレス値が高すぎてセンサー壊れたかも", "ちょっと遊んでもええ日やで",
    "今日のあなたの精神力…MAXは無理やな", "笑いでカロリー消費や", "深呼吸しても酸素足りんかも"
] * 3

# --- 生成 ---
if st.button("🧘 癒しポイントを出す"):
    num_tips = max(1, int(round(6 - stress)))
    tips_to_show = random.sample(relax_tips, k=num_tips)
    comment_out = random.choice(funny_comments)

    # --- 表示 ---
    st.subheader("🌟 今日の癒しポイント")
    for tip in tips_to_show:
        st.write(f"- {tip}")

    st.subheader("💬 今日のツッコミ")
    st.info(comment_out)

    if mood:
        st.subheader("📝 自分メモ")
        st.code(mood)

    # --- 保存 ---
    new_entry = pd.DataFrame({
        "日付": [date.today()],
        "ストレス度": [stress],
        "癒しポイント": ["; ".join(tips_to_show)],
        "ツッコミ": [comment_out],
        "メモ": [mood]
    })

    st.session_state.logs = pd.concat([st.session_state.logs, new_entry], ignore_index=True)
    st.session_state.logs.to_csv(csv_file, index=False)
    st.success("✅ 今日のデータを保存しました！")

# --- 過去ログ表示 ---
st.subheader("📚 過去の癒しログ")
if not st.session_state.logs.empty:
    st.dataframe(st.session_state.logs)
else:
    st.write("まだ記録はありません。")
