import streamlit as st
from PIL import Image


# Displaying an image
image = Image.open('data/sample.jpg')
st.image(image, caption='Beautiful piggy')

# Displaying video
video = open('data/sample.mp4', 'rb')
video_data = video.read()
st.video(video_data)

# Displaying audio
audio = open('data/sample.mp3', 'rb')
audio_data = audio.read()
st.audio(audio_data)
