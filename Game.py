import streamlit as st
import random
st.set_page_config(
    page_title="PyVerse",
    page_icon="🐍",
    layout="centered"
)

st.markdown("""
<style>
.logo {
    text-align: center;
    font-size: 90px;
    font-weight: bold;
    color: white;
}
.p {
    font-size: 130px;
    color: #FFD43B;
}
.tagline {
    text-align: center;
    font-size: 24px;
    color: #4dabf7;
    letter-spacing: 3px;
}
body {
    background-color: #0e1117;
}
</style>

<div class="logo">
    <span class="p">P</span>YVERSE
</div>

<div class="tagline">
    🐍 THE UNIVERSE OF PYTHON DEVELOPERS 🚀
</div>
""", unsafe_allow_html=True)
