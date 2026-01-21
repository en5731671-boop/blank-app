import streamlit as st
import pandas as pd
import random
import os
from datetime import date, datetime
import time

st.set_page_config(page_title="地理クイズ学習モード", layout="centered")
st.title("🌍 地理クイズ学習モード")
st.caption("正答率に応じて難易度調整＋タイマー付き学習モード")

# --- CSV保存 ---
csv_file = "geo_quiz_log.csv"
if "logs" not in st.session_state:
    if os.path.exists(csv_file):
        st.session_state.logs = pd.read_csv(csv_file)
    else:
        st.session_state.logs = pd.DataFrame(columns=["日付","問題","選択肢","正解","回答","正誤","難易度","回答時間"])

# --- サンプル問題データ（数十問に拡張可能） ---
quiz_data = [
    {"question": "日本で一番面積が大きい都道府県は？", "choices": ["北海道","東京","沖縄","大阪"], "answer": "北海道", "difficulty": 1},
    {"question": "エベレストの標高は？", "choices": ["8848m","8611m","9000m","8700m"], "answer": "8848m", "difficulty": 2},
    {"question": "カナダの首都は？", "choices": ["トロント","オタワ","モントリオール","バンクーバー"], "answer": "オタワ", "difficulty": 1},
    {"question": "アフリカで最も人口の多い国は？", "choices": ["ナイジェリア","エジプト","南アフリカ","ケニア"], "answer": "ナイジェリア", "difficulty": 2},
    {"question": "日本の最北端の島は？", "choices": ["択捉島","利尻島","礼文島","奥尻島"], "answer": "択捉島", "difficulty": 3},
    # ... 数十〜数百問に拡張可能
]

# --- 難易度調整（正答率に応じて） ---
if not st.session_state.logs.empty:
    total = len(st.session_state.logs)
    correct = st.session_state.logs['正誤'].sum()
    rate = correct / total if total>0 else 0
else:
    rate = 0.5

if rate >= 0.8:
    difficulty_level = 3  # 高正答率 → 難問
elif rate >= 0.5:
    difficulty_level = 2
else:
    difficulty_level = 1

available_questions = [q for q in quiz_data if q["difficulty"]==difficulty_level]
quiz = random.choice(available_questions)

# --- 一問一答形式 ---
st.subheader(f"難易度 {quiz['difficulty']} 問題")
st.write(quiz["question"])
user_choice = st.radio("選択してください", quiz["choices"])

# --- タイマー（例：30秒） ---
st.write("回答は30秒以内に！")
if st.button("回答"):
    start_time = datetime.now()
    
    # ここでタイマー制限を入れる場合は st.progress 等で表示可
    # 実装簡易化のためスキップ
    
    correct = user_choice == quiz["answer"]
    if correct:
        st.success("正解！🎉")
    else:
        st.error(f"不正解…正解は {quiz['answer']} です")

    elapsed_time = (datetime.now() - start_time).seconds

    # --- 保存 ---
    new_entry = pd.DataFrame({
        "日付":[date.today()],
        "問題":[quiz["question"]],
        "選択肢":[", ".join(quiz["choices"])],
        "正解":[quiz["answer"]],
        "回答":[user_choice],
        "正誤":[correct],
        "難易度":[quiz["difficulty"]],
        "回答時間":[elapsed_time]
    })
    st.session_state.logs = pd.concat([st.session_state.logs, new_entry], ignore_index=True)
    st.session_state.logs.to_csv(csv_file,index=False)

# --- 過去ログ表示 ---
st.subheader("📚 過去のログ")
if not st.session_state.logs.empty:
    st.dataframe(st.session_state.logs)
    # 正答率計算
    total = len(st.session_state.logs)
    correct = st.session_state.logs['正誤'].sum()
    st.write(f"現在の正答率: {correct}/{total} = {correct/total:.1%}")
