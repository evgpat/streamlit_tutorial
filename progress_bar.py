import streamlit as st
import time

# Progress bar
bar_p = st.progress(0)

for percentage_complete in range(100):
    time.sleep(0.1)
    bar_p.progress(percentage_complete + 1)

# Status message
# display a temporary message when executing a block of code
with st.spinner('Please wait...'):
    time.sleep(5)
st.write('Complete!')
