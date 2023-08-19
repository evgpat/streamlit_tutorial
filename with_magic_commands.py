import streamlit as st

# 1. Display text
'Hello world'

# 2. Display a title and some text to the app:
'''
# This is the document title
This is some _markdown_.
'''

# 3. Display the dataframe
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
df

# 4. Display the string 'x' and then the value of x
x = 10
'x', x

# 5. Display Matplotlib chart
import matplotlib.pyplot as plt
import numpy as np

y = np.random.normal(0, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(y, bins=20)

fig
