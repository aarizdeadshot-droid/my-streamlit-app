import streamlit as st

# Set up clean light page layout
st.set_page_config(page_title="The Aariz Game", page_icon="🎮")

# Initialize game progression state safely
if "game_started" not in st.session_state:
    st.session_state.game_started = False

st.title("🎮 The Aariz Game")
