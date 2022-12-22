## ---------------------------------------------------------- ##
## - DEKLARASI PUSTAKA -------------------------------------- ##
## ---------------------------------------------------------- ##
# pustaka untuk manipulasi data-frame
import pandas as pd
from pandas import concat
from pandas import read_csv
from pandas import read_excel
from pandas_datareader import DataReader

# pustaka untuk madnipulasi data-array
import numpy as np
from numpy import concatenate
from numpy import array

# pustaka untuk visualisasi data
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt

# pustaka dashboard
import streamlit as st

# pustaka file
from main_eda import *;

## ---------------------------------------------------------- ##
## - AKUISISI DATA ------------------------------------------ ##
## ---------------------------------------------------------- ##
# fungsi load dataset
def load_dataset():
    
    # load dataset
    df = pd.read_csv("D:/latihan-time-series/dataset/BTC-USD.csv");
    
    # set index tanggal
    df = df.set_index("Date");

    # return value
    return df;

# membaca dataset csv
dataset = load_dataset();

## ---------------------------------------------------------- ##
## - Main Dashboard ----------------------------------------- ##
## ---------------------------------------------------------- ##
# set config streamlit
st.set_page_config(page_title="My Dashboard", layout="wide", initial_sidebar_state="auto");

# st.sidebar.title("My Dashboard");
# with st.sidebar:
#     st.title("My Dashboard");
#     st.selectbox('Choose Dataset', ('Bitcoin USD (BTC-USD)', 'Microsoft Corporation (MSFT)', 'Apple Inc. (AAPL)', 'Google Inc. (GOOG)', 'Amazon.com Inc. (AMZN)'));
#     st.date_input("Start date");
#     st.date_input("End date");
#     st.selectbox('Choose Algorithm', ('LSTM-RNN', 'GRU-RNN', 'Xgboost', 'Prophet'));
#     st.button('Submit');

# set a title dashboard
st.markdown('## Stock Price Prediction with LSTM - GRU - Xgboost - Prophet');

# show a dataset
st.subheader("Dataset of Bitcoin USD (BTC-USD)");
st.dataframe(dataset, use_container_width=True);

# multiple plot time OHLC
st.subheader("Data Visualization Open-High-Low-Close (OHLC)");
st.plotly_chart(px.line(dataset, x=dataset.index, y=["Close", "Open", "High", "Low"], color_discrete_sequence=["blue", "green", "orange", "red"]), use_container_width=True);

# set two columns
fig1, fig2 = st.columns(2, gap="large");
with fig1:
    st.text("Open price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='Open', color_discrete_sequence=["blue"]), use_container_width=True);
with fig2:
    st.text("Close price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='Close', color_discrete_sequence=["green"]), use_container_width=True);

# set two columns
fig1, fig2 = st.columns(2, gap="large");
with fig1:
    st.text("High price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='High', color_discrete_sequence=["orange"]), use_container_width=True);
with fig2:
    st.text("Low price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='Low', color_discrete_sequence=["red"]), use_container_width=True);

# a container eda
st.subheader("Exploratory Data Analysis (EDA)");

# set tab-index
t2015, t2016, t2017, t2018, t2019, t2020, t2021 = st.tabs(["EDA 2015", "EDA 2016", "EDA 2017", "EDA 2018", 'EDA 2019', "EDA 2020", "EDA 2021"]);

with t2015:
    # dataset eda 2015
    date_start = "2015-01-01";
    date_end = "2015-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));

with t2016:
    # dataset eda 2016
    date_start = "2016-01-01";
    date_end = "2016-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));

with t2017:
    # dataset eda 2017
    date_start = "2017-01-01";
    date_end = "2017-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));

with t2018:
    # dataset eda 2016
    date_start = "2018-01-01";
    date_end = "2018-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));

with t2019:
    # dataset eda 2019
    date_start = "2019-01-01";
    date_end = "2019-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));

with t2020:
    # dataset eda 2016
    date_start = "2020-01-01";
    date_end = "2020-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));

with t2021:
    # dataset eda 2021
    date_start = "2021-01-01";
    date_end = "2021-12-31";
    df_eda = set_year(dataset, date_start, date_end);

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Close"], color_discrete_sequence=["#0051ee"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Open"], color_discrete_sequence=["#20B2AA"], text_auto='.2s'));

    c1, c2 = st.columns(2, gap="large");
    with c1:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["High"], color_discrete_sequence=["#FF8C00"], text_auto='.2s'));
    with c2:
        st.plotly_chart(px.bar(df_eda, x=df_eda.index, y=df_eda["Low"], color_discrete_sequence=["#DC143C"], text_auto='.2s'));