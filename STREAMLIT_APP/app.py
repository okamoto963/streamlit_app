import streamlit as st
import pandas as pd
from pandas import DataFrame as df
import plotly as plt
import numpy as np

st.title("tameshi")

df1 = pd.read_csv("CPI.csv", encoding="shift_jis")

#st.table(df1)  CSVが読み込めているか確認

#with st.sidebar:
