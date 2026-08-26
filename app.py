import streamlit as st

# Configure the web page layout
st.set_page_config(page_title="My Python Introduction Web ", page_icon="🐍")

st.title("Welcome to My Streamlit Web App! 🚀")
st.write("This interactive interface was built 100% using Python code.")
st.write("I am  PYTHON Developer")

# Create an interactive text input box
user_name = st.text_input("Enter your name:", placeholder="Type here...")

# Create an interactive button
if st.button("Submit Name"):
    if user_name:
        st.success(f"Hello, {user_name}! Welcome to your python-powered website.")
    else:
        st.warning("Please enter a name first!")
st.write("where do you live")
# Create an interactive text input box
user_name = st.text_input("Enter your place:", placeholder="Type here...")

# Create an interactive button
if st.button("Submit Place"):
    if user_name:
        st.success(f"good, {user_name}!.")
    else:
        st.warning("Please enter a place first!")
st.write("Are you enjoying my game")
# Create an interactive text input box
user_name = st.text_input("Enter:", placeholder="Type here...")

# Create an interactive button
if st.button("Submit Answer"):
    if user_name:
        
        st.success(f"Good,.")
st.write("hard work on this web 50 lines code and this output")

import streamlit as st

# Replace with the exact live web address of your subpage
st.link_button("Open Analytics Page", "https://streamlit.app")
