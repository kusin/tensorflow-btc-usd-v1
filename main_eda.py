import pandas as pd;
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# func set range year
def set_year(df_year, date_start="", date_end=""):

    # df_year = df_year.iloc[(df_year.index >= '2015-01-01') & (df_year.index <= '2015-12-31')];
    # df_year = df_year.groupby(pd.Grouper(freq="M")).mean();
    # df_year =  df_year.resample("M").sum();
    
    df_year.index = pd.to_datetime(df_year.index, format="%Y-%m-%d");
    df_year = df_year.iloc[(df_year.index >= date_start) & (df_year.index <= date_end)];
    df_year =  df_year.resample("M").sum();
   
    return df_year;

# # set two columns
# fig1, fig2 = st.columns(2, gap="small");
# with fig1:
#     fig = go.Figure();
#     fig.add_trace(go.Bar(
#         x=df_eda.index,
#         y=df_eda['Open'],
#         name='Stock Open Price',
#         marker_color='crimson'
#     ));
#     fig.add_trace(go.Bar(
#         x=df_eda.index,
#         y=df_eda['Close'],
#         name='Stock Close Price',
#         marker_color='lightsalmon'
#     ));
#     st.plotly_chart(fig);

# with fig2:
#     fig = go.Figure();
#     fig.add_trace(go.Bar(
#         x=df_eda.index,
#         y=df_eda['High'],
#         name='Stock Open Price',
#         marker_color='rgb(0, 153, 204)'
#     ));
#     fig.add_trace(go.Bar(
#         x=df_eda.index,
#         y=df_eda['Low'],
#         name='Stock Close Price',
#         marker_color='rgb(255, 128, 0)'
#     ));
#     st.plotly_chart(fig);
