pip install streamlit requests
import streamlit as st
import requests
from datetime import datetime

# Force a clean, standard light theme layout
st.set_page_config(page_title="The Holy Quran & Namaz Times", page_icon="📖", layout="wide")

# Global CSS injector to guarantee white page background and dark charcoal text
st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF !important;
        }
        h1, h2, h3, h4, h5, h6, p, span, label, .stSelectbox div {
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
        .prayer-box {
            background-color: #F8F9FA;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #E0E0E0;
            text-align: center;
            margin: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🧭 Navigation")
app_mode = st.sidebar.radio("Go to:", ["📖 Read Quran", "🕌 Namaz Times"])

# --- MODE 1: READ QURAN ---
if app_mode == "📖 Read Quran":
    st.title("📖 The Holy Quran")
    st.write("Read all 114 Surahs with side-by-side English translations.")
    
    # Secure live API fetching for the dropdown menu
    @st.cache_data(show_spinner=False)
    def fetch_surahs():
        try:
            res = requests.get("https://alquran.cloud", timeout=10)
            if res.status_code == 200:
                return res.json()["data"]
        except Exception:
            pass
        return None

    surah_list = fetch_surahs()

    if surah_list:
        # Build dropdown options mapping
        surah_map = {f"{s['number']}. {s['englishName']} ({s['name']})": s['number'] for s in surah_list}
        selected_surah = st.selectbox("Select a Surah to read:", list(surah_map.keys()))
        surah_id = surah_map[selected_surah]
        
        # Secure concurrent content fetching (Arabic text + Sahih International English Translation)
        @st.cache_data(show_spinner=False)
        def fetch_surah_content(number):
            try:
                ar_url = f"https://alquran.cloud/{number}/quran-uthmani"
                en_url = f"https://alquran.cloud/{number}/en.sahih"
                
                ar_res = requests.get(ar_url, timeout=10).json()
                en_res = requests.get(en_url, timeout=10).json()
                
                return ar_res["data"], en_res["data"]
            except Exception:
                return None, None

        arabic_data, english_data = fetch_surah_content(surah_id)
        
        if arabic_data and english_data:
            st.markdown(f"### ✨ Surah {arabic_data['englishName']} — {arabic_data['name']}")
            st.write(f"**Meaning:** {arabic_data['englishNameTranslation']} | **Verses:** {len(arabic_data['ayahs'])}")
            st.markdown("---")
            
            # Print Verses Loop
            for i in range(len(arabic_data['ayahs'])):
                # Clean up Bismillah repetition for display clarity if needed
                ayah_text = arabic_data['ayahs'][i]['text']
                
                # Right-aligned sharp black Arabic Text
                st.markdown(
                    f'<p style="text-align: right; font-size: 28px; font-family: sans-serif; direction: rtl; line-height: 2.0; color: #1A1A1A; margin-bottom: 5px;">'
                    f'{ayah_text} ﴿{arabic_data["ayahs"][i]["numberInSurah"]}﴾'
                    f'</p>', 
                    unsafe_allow_html=True
                )
                # Left-aligned English translation
                st.markdown(
                    f'<p style="text-align: left; font-size: 16px; color: #444444; margin-bottom: 25px;">'
                    f'<b>Verse {arabic_data["ayahs"][i]["numberInSurah"]}:</b> {english_data["ayahs"][i]["text"]}'
                    f'</p>', 
                    unsafe_allow_html=True
                )
                st.markdown("<hr>", unsafe_allow_html=True)
        else:
            st.error("Could not fetch Surah text. Please check your internet connection.")
    else:
        st.error("Failed to connect to the Quran API. Please try reloading the page.")

# --- MODE 2: NAMAZ TIMES ---
else:
    st.title("🕌 Namaz (Prayer) Times")
    st.write("Get accurate daily prayer timings for any city worldwide.")
    
    # Input controls
    col1, col2 = st.columns(2)
    with col1:
        city = st.text_input("Enter City Name:", value="Islamabad")
    with col2:
        country = st.text_input("Enter Country Name:", value="Pakistan")
        
    @st.cache_data(show_spinner=False)
    def fetch_prayer_times(city_name, country_name):
        try:
            today_date = datetime.now().strftime("%d-%m-%Y")
            url = f"https://aladhan.com{today_date}?city={city_name}&country={country_name}&method=2"
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                return res.json()["data"]
        except Exception:
            pass
        return None

    if city and country:
        prayer_data = fetch_prayer_times(city.strip(), country.strip())
        
        if prayer_data:
            timings = prayer_data["timings"]
            meta = prayer_data["meta"]
            date_info = prayer_data["date"]
            
            st.markdown(f"### 📍 Timings for {city.capitalize()}, {country.capitalize()}")
            st.write(f"**Islamic Date:** {date_info['hijri']['day']} {date_info['hijri']['month']['en']} {date_info['hijri']['year']} AH")
            st.write(f"**Calculation Method:** {meta['method']['name']}")
            st.markdown("---")
            
            # Display grid arrangement
            p_cols = st.columns(5)
            prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
            
            for idx, p_name in enumerate(prayers):
                with p_cols[idx]:
                    st.markdown(f"""
                        <div class="prayer-box">
                            <h4 style="margin:0; color:#1A1A1A;">{p_name}</h4>
                            <p style="margin:10px 0 0 0; font-size:20px; font-weight:bold; color:#000000;">{timings[p_name]}</p>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Could not retrieve prayer times. Please verify the city spelling or check your connection.")
streamlit run app.py
