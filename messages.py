import streamlit as st

# Show celebratory balloons
st.balloons()

# Show an error message
st.error("An Error was encountered")

# Display a warning message
st.warning("Incompatible data point!")

# Display informational messages
st.info("Page is refreshed every 2 hours")

# Display success messages
st.success("Record found!")

# Display an exception in your application
exp = ValueError('This is an exception of type ValueError')
st.exception(exp)
