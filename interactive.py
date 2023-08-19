import streamlit as st
import datetime

# Button
st.button("Click here")

# Check box
selected = st.checkbox("Accept terms")

# Select box
option = st.selectbox(
     'How would you like to receive your package?',
     ('By air', 'By sea', 'By rail'))
st.write('You selected:', option)

# Date input
day = st.date_input(
     "When is your birthday?",
     datetime.date(2022, 7, 6))
st.write('Your birthday is:', day)

# Multi select
selections = st.multiselect("Purchase", ["oranges", "apples", "bananas"])

# Number input
choice = st.number_input("Choose a number", 0, 50)

# Text area
text = st.text_area("Start typing")

# Time input
time = st.time_input("Dinner time")

# File upload
data = st.file_uploader("Share excel file")
