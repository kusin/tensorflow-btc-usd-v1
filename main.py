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

# pustaka untuk waktu komputasi
import time
from datetime import datetime

# pustaka untuk visualisasi data
import seaborn as sns
from matplotlib import pyplot
from matplotlib import pyplot as plt

# pustaka untuk visualisasi acf dan pacf
import scipy.stats as sc
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf

# pustaka untuk membuat data latih dan data uji.
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# pustaka untuk membuat model prediksi LSTM-RNN
import itertools
import tensorflow as tf
from keras.utils import Sequence
from keras.models import Sequential
from keras.layers import SimpleRNN
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.optimizers import Adam, Adamax, RMSprop, SGD

# early stoping
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint

# pustaka untuk  evaluasi model prediksi
import math
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# pustaka dashboard
import streamlit as st
import plotly.express as px

## ---------------------------------------------------------- ##
## - CONFIG ------------------------------------------------- ##
## ---------------------------------------------------------- ##
# set config streamlit
st.set_page_config(page_title="My Dashboard", layout="wide", initial_sidebar_state="auto");

## ---------------------------------------------------------- ##
## - AKUISISI DATA ------------------------------------------ ##
## ---------------------------------------------------------- ##
# fungsi load dataset
@st.cache
def load_dataset():
    # return value
    return pd.read_csv("D:/latihan-time-series/dataset/BTC-USD.csv");

# membaca dataset csv
dataset = load_dataset();

# set index tanggal
# dataset = dataset.set_index("Date");


## ---------------------------------------------------------- ##
## - Sidebar ------------------------------------------------- ##
## ---------------------------------------------------------- ##
# st.sidebar.title("My Dashboard");
with st.sidebar:
    st.title("My Dashboard");
    st.selectbox('Choose Dataset', ('Bitcoin USD (BTC-USD)', 'Microsoft Corporation (MSFT)', 'Apple Inc. (AAPL)', 'Google Inc. (GOOG)', 'Amazon.com Inc. (AMZN)'));
    st.date_input("Start date");
    st.date_input("End date");
    st.selectbox('Choose Algorithm', ('LSTM-RNN', 'GRU-RNN', 'Xgboost', 'Prophet'));
    
    st.button('Submit');
    

## ---------------------------------------------------------- ##
## - Header ------------------------------------------------- ##
## ---------------------------------------------------------- ##
# set a title dashboard
st.markdown('## Stock Price Prediction with LSTM - GRU - Xgboost - Prophet');


## ---------------------------------------------------------- ##
## - Content ------------------------------------------------ ##
## ---------------------------------------------------------- ##
# show a dataset
st.text("Dataset of Bitcoin USD (BTC-USD)");
st.dataframe(dataset, use_container_width=True);

# plot time series a colums open and close
st.plotly_chart(px.line(dataset, x='Date', y='Open', title='Open price bitcoin'),
                use_container_width=True, sharing="streamlit", theme="streamlit");

st.plotly_chart(px.line(dataset, x='Date', y='Close', title='Close price bitcoin'),
                use_container_width=True, sharing="streamlit", theme="streamlit");

st.plotly_chart(px.line(dataset, x='Date', y='High', title='High price bitcoin'),
                use_container_width=True, sharing="streamlit", theme="streamlit");

st.plotly_chart(px.line(dataset, x='Date', y='Low', title='Low price bitcoin'),
                use_container_width=True, sharing="streamlit", theme="streamlit");
