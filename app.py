import streamlit as st
import requests

# Set page configuration to wide mode
st.set_page_config(page_title="The Holy Quran", page_icon="📖", layout="wide")

# Inject clean white background and dark text styling
st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF !important;
        }
        h1, h2, h3, p, span, label, .stSelectbox div {
            color: #1A1A1A !important;
        }
        div[data-baseweb="select"] > div {
            background-color: #F8F9FA !important;
            color: #1A1A1A !important;
            border: 1px solid #CCCCCC !important;
        }
        hr {
            border-top: 1px solid #E0E0E0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title Headers
st.title("📖 The Holy Quran")
st.write("Read and study all 114 Surahs with text and translation.")
st.markdown("---")

# 1. Fetch the complete list of 114 Surahs from the API
@st.cache_data(show_spinner=False)
def get_surah_list():
    url = "https://alquran.cloud"
    try:
        response = requests.get(url, timeout=10).json()
        return response["data"]
    except Exception:
        return None

surahs = get_surah_list()

if surahs:
    # Build a dictionary to map names to Surah numbers
    surah_options = {f"{s['number']}. {s['englishName']} ({s['name']})": s['number'] for s in surahs}
    
    # Dropdown menu to pick a Surah
    selected_surah_name = st.selectbox("Search or Select a Surah:", list(surah_options.keys()))
    surah_num = surah_options[selected_surah_name]

    # 2. Fetch Arabic verses and English translation concurrently
    @st.cache_data(show_spinner=False)
    def get_surah_text(number):
        arabic_url = f"https://alquran.cloud/{number}/quran-uthmani"
        english_url = f"https://alquran.cloud/{number}/en.sahih"
        try:
            ar_res = requests.get(arabic_url, timeout=10).json()["data"]
            en_res = requests.get(english_url, timeout=10).json()["data"]
            return ar_res, en_res
        except Exception:
            return None, None

    ar_data, en_data = get_surah_text(surah_num)
    
    if ar_data and en_data:
        arabic_ayahs = ar_data["ayahs"]
        english_ayahs = en_data["ayahs"]

        # Surah metadata layout heading
        st.markdown(f"### ✨ Surah {ar_data['englishName']} ({ar_data['name']})")
        st.write(f"**Meaning:** {ar_data['englishNameTranslation']} | **Total Verses:** {len(arabic_ayahs)}")
        st.markdown("---")

        # 3. Print the verses on screen loop
        for i in range(len(arabic_ayahs)):
            # Crisp black Arabic typography right-aligned
            st.markdown(
                f'<p style="text-align: right; font-size: 28px; font-family: sans-serif; direction: rtl; line-height: 2.0; color: #1A1A1A; margin-bottom: 5px;">'
                f'{arabic_ayahs[i]["text"]} ﴿{arabic_ayahs[i]["numberInSurah"]}﴾'
                f'</p>', 
                unsafe_allow_html=True
            )
            
            # Crisp black translation text left-aligned
            st.markdown(
                f'<p style="text-align: left; font-size: 16px; color: #333333; margin-bottom: 25px;">'
                f'<b>Verse {arabic_ayahs[i]["numberInSurah"]}:</b> {english_ayahs[i]["text"]}'
                f'</p>', 
                unsafe_allow_html=True
            )
            st.markdown("<hr>", unsafe_allow_html=True)
    else:
        st.error("Failed to load Surah content. Please check your network connection.")
else:
    st.info("🔄 Connecting to the Quran servers...")
