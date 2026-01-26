import streamlit as st
import pandas as pd
from pandas import DataFrame as df
import plotly as plt
import numpy as np

st.title("CSV 読み込みチェック")

try:
    df = pd.read_csv("ma030000.csv", encoding="shift_jis")
    st.success("CSV を正常に読み込めました")
    st.write(df.head())
    st.write(df.shape)
except Exception as e:
    st.error("CSV の読み込みに失敗しました")
    st.write(str(e))