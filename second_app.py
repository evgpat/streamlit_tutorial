import streamlit as st
import pandas as pd
import plotly.express as px

df = st.cache_data(pd.read_csv)("data/football.csv")

clubs = st.sidebar.multiselect(
    'Show Player for clubs?',
    df['Club'].unique()
)

nationalities = st.sidebar.multiselect(
    'Show Player from Nationalities?',
    df['Nationality'].unique()
)

filtred = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(filtred)

# Create distplot with custom bin_size
fig = px.scatter(filtred, x='Overall', y='Age', color='Name')

# Plot!
st.plotly_chart(fig)
