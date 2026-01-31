import streamlit as st
import pandas as pd
from pandas import DataFrame as df
import plotly as plt
import numpy as np

st.title("CPI可視化app")

df = pd.read_csv("CPI.csv", encoding="shift_jis")

st.subheader("CPIとは")
st.write("CPIとは、消費者が購入する商品やサービスの価格の変動を測定する経済指標を表しています。")

st.subheader('概要と目的')
st.write('このアプリは、品目ごとの価格変動をグラフにして可視化することで経済の背景を学ぶことを目的としています。')

st.subheader('使い方')
st.write('はじめにCPIの変動を調べたい品目を選択してください。これにより選択した品目のCPIの変動をグラフで表示します。選択した品目が1つである場合、選択した品目の棒グラフ及び折れ線グラフを、選択した品目が複数ある場合、選択した品目全ての折れ線グラフを表示します。')
#st.table(df1)  # CSVが読み込めているか確認

# アプリの概要
# 

with st.sidebar:
  items = st.multiselect(
     '表示したい項目を選んでください(複数選択可能)',
     df.columns.tolist()
   )
  
if items:
   st.dataframe(df[items])