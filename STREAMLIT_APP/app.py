import os
print("FILES IN CLOUD:", os.listdir("."))



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import plotly.graph_objects as go
matplotlib.rcParams['font.family'] = 'MS Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

st.set_page_config(layout="wide")
st.title("CPI可視化app")

df = pd.read_csv("CPI.csv", encoding="utf-8")



# 必須構成　その１　(アプリの概要・目的・使い方)
with st.expander("アプリの説明（クリックで表示）"):
    st.subheader("CPIとは")
    st.write("CPIとは、消費者が購入する商品やサービスの価格の変動を測定する経済指標を表しています。")

    st.divider()

    st.subheader('概要と目的')
    st.write('このアプリは、品目ごとの価格変動をグラフにして可視化することで経済の背景を学ぶことを目的としています。')

    st.divider()

    st.subheader('使い方')
    st.markdown(
    "はじめにCPIの変動を調べたい品目を選択してください。  \n"
    "選択した品目が1つである場合、選択した品目の棒グラフ及び折れ線グラフを、  \n"
    "選択した品目が複数ある場合、選択した品目全ての折れ線グラフを表示します。"
)

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
# 1つのみ選択(2種類のグラフ表示)import plotly.graph_objects as go

if len(items) == 1:
    item = items[0]

    fig = go.Figure()

    # 折れ線
    fig.add_trace(go.Scatter(
        x=df['年'], y=df[item],
        mode='lines+markers',
        name=item
    ))

    # 棒グラフ
    fig.add_trace(go.Bar(
        x=df['年'], y=df[item],
        name=item,
        opacity=0.6
    ))

    fig.update_layout(
        width=900, height=500,
        xaxis_title="年",
        yaxis_title="指数"
    )

    st.plotly_chart(fig, use_container_width=True)

elif len(items) >= 2:
    fig = go.Figure()

    for item in items:
        fig.add_trace(go.Scatter(
            x=df['年'], y=df[item],
            mode='lines+markers',
            name=item
        ))

    fig.update_layout(
        width=900, height=500,
        xaxis_title="年",
        yaxis_title="指数",
        hovermode="x unified" 
    )

    st.plotly_chart(fig, use_container_width=True)

with st.expander("可視化結果の説明(クリックで表示)"):
    st.markdown(
    "数値が右肩上がりの場合 → 物価が上昇している。  \n"
    "数値が右肩下がりの場合 → 物価が下降している。  \n"
    "数値が停滞している場合 → 物価が変化していない。  \n"
    "<span style='color:red;'>※これは解釈の例であり必ずとは言い切れません。</span>",
    unsafe_allow_html=True
)