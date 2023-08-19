import streamlit as st
import pandas as pd

# students and marks
students = ["Amelia Kami", "Antoinne Mark", "Peter Zen", "North Kim"]
marks = [82, 76, 96, 68]

df = pd.DataFrame()
df["Student Name"] = students
df["Marks"] = marks

# display dataframe
st.dataframe(df)

# static table
st.table(df)

# metrics
st.metric("KPI", 56, 3)

# json
st.json(df.to_dict())
