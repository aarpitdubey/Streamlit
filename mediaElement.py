import streamlit as st

# Adding audio 
audio_file = open('Path\\file.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# video 

video_file = open('Path\\file.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)