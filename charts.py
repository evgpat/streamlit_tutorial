import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


# Matplotlib
arr = np.random.normal(1, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)
plt.grid()
st.pyplot(fig)

# Plotly
# This data frame has 244 rows, but 4 unique entries for the `day` variable
df = px.data.tips()
fig = px.pie(df, values='tip', names='day')
st.plotly_chart(fig, use_container_width=True)
