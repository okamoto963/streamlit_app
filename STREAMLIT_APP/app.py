import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'MS Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False


st.title("CPI可視化app")

df = pd.read_csv("CPI.csv", encoding="shift_jis")



# 必須構成　その１　(アプリの概要・目的・使い方)
st.subheader("CPIとは")
st.write("CPIとは、消費者が購入する商品やサービスの価格の変動を測定する経済指標を表しています。")

st.subheader('概要と目的')
st.write('このアプリは、品目ごとの価格変動をグラフにして可視化することで経済の背景を学ぶことを目的としています。')

st.subheader('使い方')
st.write('はじめにCPIの変動を調べたい品目を選択してください。',
         '選択した品目が1つである場合、選択した品目の棒グラフ及び折れ線グラフを、',
         '選択した品目が複数ある場合、選択した品目全ての折れ線グラフを表示します。')

#st.table(df)  # CSVが読み込めているか確認


with st.sidebar:
  items = st.multiselect(
     '表示したい項目を選んでください(複数選択可能)',
     df.columns[2:]
   )
# UI その１  
if not items:
   st.warning('品目を1つ以上選択してください(複数選択可)')
   st.stop()
# 1つのみ選択(2種類のグラフ表示)
if len(items) == 1:
    item = items[0]
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df['年'], df[item], marker='o')
    ax.bar(df['年'], df[item], alpha=0.6)

    ax.set_xlabel("年")
    ax.set_ylabel("指数")
    ax.grid(True)
    
    st.pyplot(fig) # グラフの表示

elif len(items) >= 2:
    fig, ax = plt.subplots(figsize=(12, 6))

    for item in items:
        ax.plot(df['年'], df[item], marker='o', label=item)

    ax.set_xlabel("年")
    ax.set_ylabel("指数")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)