import streamlit as st
import pandas as pd
from pandas import DataFrame as df
import plotly as plt
import numpy as np

st.title('test')
pd.read_csv('STREAMLIT_APP\ma030000.csv')
pd.read_csv('STREAMLIT_APP\表6-2.csv')

df.head()
df.shape
df.dtypes
df.isna().sum()