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
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="The Holy Quran - By Para (Juz)",
    page_icon="📖",
    layout="wide"
)

# 2. Pure Black & White Custom Theme CSS
st.markdown("""
    <style>
    /* Absolute black and white styling */
    .stApp {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: #000000 !important;
        font-family: 'serif';
    }
    /* Sidebar styling override */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #E0E0E0;
    }
    /* Elegant Right-to-Left Arabic text block styling */
    .para-container {
        direction: rtl;
        text-align: justify;
        font-family: 'Traditional Arabic', 'Scheherazade New', 'Amiri', serif;
        font-size: 32px;
        line-height: 2.3;
        color: #000000 !important;
        padding: 30px;
        background-color: #FFFFFF;
        border: 1px solid #000000;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    /* Surah Heading Divider Block */
    .surah-header {
        text-align: center;
        background-color: #000000;
        color: #FFFFFF !important;
        font-size: 24px;
        padding: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
        border-radius: 4px;
    }
    .ayah-num {
        font-size: 20px;
        color: #555555;
        margin-left: 6px;
        margin-right: 6px;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cached API Fetcher for Para Data
@st.cache_data(show_spinner="Loading Para Text...")
def fetch_para_data(juz_number):
    try:
        # Fetching Uthmani Text representation for the specific Juz
        url = f"https://alquran.cloud{juz_number}/quran-uthmani"
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()["data"]
    except Exception as e:
        return None
    return None

# 4. Sidebar Selection Layout
st.sidebar.title("📖 Navigation")
para_num = st.sidebar.selectbox(
    "Select Para (Juz):",
    options=list(range(1, 31)),
    format_func=lambda x: f"Para {x}"
)

# 5. Main Screen Render
st.title(f"📖 Juz / Para {para_num}")
st.caption("Complete text layout in crisp black & white typography")
st.markdown("---")

# Fetch and process text data
data = fetch_para_data(para_num)

if data:
    ayahs = data.get("ayahs", [])
    current_surah = ""
    
    # We will build out HTML dynamically to support correct reading formatting blocks
    html_buffer = ""
    
    for ayah in ayahs:
        surah_name = ayah["surah"]["name"]
        text = ayah["text"]
        
        # Detect if a new Surah boundary begins inside this Para
        if surah_name != current_surah:
            # If a previous block was running, close it out
            if html_buffer != "":
                html_buffer += "</div>"
                st.markdown(html_buffer, unsafe_allow_html=True)
                html_buffer = ""
            
            # Print the header divider banner for the new Surah
            current_surah = surah_name
            st.markdown(f'<div class="surah-header">{current_surah}</div>', unsafe_allow_html=True)
            
            # Open up a clean paragraph content block container
            html_buffer = '<div class="para-container">'
            
            # Formatting handling for Bismillah presentation on start of chapters
            if ayah["numberInSurah"] == 1 and text.startswith("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ") and ayah["surah"]["number"] != 1:
                st.markdown("<h3 style='text-align: center; color: black; margin-bottom: 20px;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</h3>", unsafe_allow_html=True)
                # Strip out duplicate string reference from running text flow
                text = text.replace("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", "").strip()
        
        # Append active verse character string tokens with verse circle indicator numbers
        html_buffer += f'{text} <span class="ayah-num">﴿{ayah["numberInSurah"]}﴾</span> '
    
    # Close out final loop container if contents remain
    if html_buffer != "":
        html_buffer += "</div>"
        st.markdown(html_buffer, unsafe_allow_html=True)

else:
    st.error("Failed to load Para data. Please verify your internet connection connection setup.")

# 6. Bottom Navigation Controls
st.markdown("<br>", unsafe_allow_html=True)
col_prev, col_spacer, col_next = st.columns([1, 4, 1])

with col_prev:
    if para_num > 1:
        if st.button("⬅️ Previous Para"):
            # Update via sidebar state trigger
            st.info("Use Sidebar select option to jump back instantly!")

with col_next:
    if para_num < 30:
        if st.button("Next Para ➡️"):
            st.info("Use Sidebar select option to step forward instantly!")
@st.cache_data(show_spinner="Loading Para Text...")
def fetch_para_data(juz_number):
    # Primary API Endpoint
    url_primary = f"https://alquran.cloud{juz_number}/quran-uthmani"
    # Backup Mirror Endpoint if primary fails
    url_backup = f"https://islamic.network{juz_number}/quran-uthmani"
    
    try:
        # Try Primary Domain
        response = requests.get(url_primary, timeout=10, verify=False)
        if response.status_code == 200:
            return response.json()["data"]
    except Exception:
        try:
            # Fallback to Mirror Domain if primary is busy
            response = requests.get(url_backup, timeout=10, verify=False)
            if response.status_code == 200:
                return response.json()["data"]
        except Exception:
            return None
    return None
