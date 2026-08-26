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

# 1. Page Configuration for a clean, minimalist layout
st.set_page_config(
    page_title="The Holy Quran",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Inject Black & White Minimalist Theme Custom CSS
st.markdown("""
    <style>
    /* Force high-contrast black and white backgrounds */
    .stApp {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    /* Style all text and headers to pure black */
    h1, h2, h3, p, label, .stMarkdown {
        color: #000000 !important;
        font-family: 'serif';
    }
    /* Customize the slider element to match the grayscale theme */
    div[data-baseweb="slider"] {
        background-color: #E0E0E0;
    }
    div[role="slider"] {
        background-color: #000000 !important;
    }
    /* Center and crisp the Quran page image rendering */
    .quran-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 4px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }
    img {
        max-width: 100%;
        height: auto;
        filter: grayscale(100%) contrast(120%);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Application Title
st.title("📖 The Holy Quran")
st.caption("All 604 pages in high-contrast black and white layout")

# 4. Navigation Control (Using a Slider + Number Input for easy 604-page traversal)
col1, col2 = st.columns([3, 1])

with col1:
    page_slider = st.slider("Slide to navigate pages", min_value=1, max_value=604, value=1)

with col2:
    page_input = st.number_input("Page No.", min_value=1, max_value=604, value=page_slider)

# Sync the slider and number input together
current_page = page_input if page_input != page_slider else page_slider

# 5. Fetching and Displaying the Page
# We use a reliable, publicly indexed high-resolution repository for the 604 Madinah pages
# The string formatting Z03d pads page 1 into '001', page 55 into '055', etc.
archive_url = f"https://archive.org{current_page:03d}.png"

st.markdown("---")

# Render the image container
st.markdown(f"""
    <div class="quran-container">
        <!-- Grayscale filter applied via CSS ensures pure black & white presentation -->
        <img src="{archive_url}" alt="Quran Page {current_page}" />
    </div>
""", unsafe_allow_html=True)

# 6. Footer Layout Navigation Buttons
st.markdown("<br>", unsafe_allow_html=True)
foot_col1, foot_col2, foot_col3 = st.columns([1, 2, 1])

with foot_col1:
    if st.button("⬅️ Previous") and current_page > 1:
        st.query_params["page"] = str(current_page - 1)
        st.rerun()

with foot_col3:
    if st.button("Next ➡️") and current_page < 604:
        st.query_params["page"] = str(current_page + 1)
        st.rerun()
