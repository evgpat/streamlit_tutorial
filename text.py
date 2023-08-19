import streamlit as st

# Title
st.title("Document Title")

# Header
st.header("Article header", anchor=None)

# Subheader
st.subheader("Article subheader")

# Text
st.text("This is a text!")

# Markdown
st.markdown('Streamlit is **_very_ cool**.')

# Code
st.code("y = mx + c")

# Code (specify language)
code = '''def cal_average(numbers):
    sum_number = 0
    for t in numbers:
        sum_number = sum_number + t           

    average = sum_number / len(numbers)
    return average'''
st.code(code, language='python')

# Latex
st.latex("\ int a y^2 \ , dy")
