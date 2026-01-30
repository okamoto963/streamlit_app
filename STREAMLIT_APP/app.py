import streamlit as st
import pandas as pd
from pandas import DataFrame as df
import plotly as plt
import numpy as np

st.title("都道府県別の人口と交通事故件数の関係")

df1 = pd.read_csv("令和6年人口動態統計.csv", encoding="shift_jis")
df2 = pd.read_csv("表6-2.csv",encoding="shift_jis")

with st.sidebar:
