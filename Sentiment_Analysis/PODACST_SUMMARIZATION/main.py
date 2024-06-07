from api_communication import *
import streamlit as st

st.title('Podcast Summaries')
st.sidebar.text_input("Please input an episode id")
st.sidebar.button("Get podcast summary!")

get_episode_audio_url("f50a202106d5472388a9f555518551a4")
