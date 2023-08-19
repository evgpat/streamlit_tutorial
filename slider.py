import streamlit as st
from datetime import time


# слайдер
st.slider(
    "label",
    min_value=5,
    max_value=25,
    value=20,
    step=None,
)

# получение значения из слайдера
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# интервальный слайдер
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(17, 45))
)
st.write("You're scheduled for:", appointment)
