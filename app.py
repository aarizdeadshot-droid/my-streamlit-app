import streamlit as st

# Configure the browser tab
st.set_page_config(page_title="Aariz's Website", page_icon="🚀")

# Title and introduction
st.title("Welcome to My Website!")
st.subheader("Hi, I'm Aariz.")
st.write("This website is running completely on Python using Streamlit.")

# Add an interactive button
if st.button("Click Me"):
    st.balloons()  # This drops fun celebratory balloons down your screen!
    st.success("Thanks for testing my app!")
streamlit run app.py
st.write("op op")
