import requests
import streamlit as st

st.set_page_config(
    page_title="Al-Quran Digital", page_icon="📖", layout="wide"
)

st.title("📖 Digital Al-Quran App")
st.write("Read the Holy Quran with Arabic text and English translation.")


@st.cache_data
def get_surahs():
  url = "http://alquran.cloud"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()["data"]
  return []


@st.cache_data
def get_ayahs(surah_number):
  # Fetch Arabic and English translation (Sahih International)
  arabic_url = f"http://alquran.cloud/{surah_number}/ar.alafasy"
  english_url = f"http://alquran.cloud/{surah_number}/en.sahih"

  res_ar = requests.get(arabic_url)
  res_en = requests.get(english_url)

  if res_ar.status_code == 200 and res_en.status_code == 200:
    return (
        res_ar.json()["data"]["ayahs"],
        res_en.json()["data"]["ayahs"],
        res_ar.json()["data"]["englishName"],
    )
  return [], [], ""


surahs = get_surahs()

if surahs:
  surah_names = {f"{s['number']}. {s['englishName']} ({s['name']})": s['number'] for s in surahs}
  selected_choice = st.sidebar.selectbox("Select Surah", list(surah_names.keys()))
  selected_surah_num = surah_names[selected_choice]

  arabic_ayahs, english_ayahs, surah_name = get_ayahs(selected_surah_num)

  st.header(f"Surah {surah_name}")

  for ar, en in zip(arabic_ayahs, english_ayahs):
    st.markdown(f"### **({ar['numberInSurah']})** {ar['text']}")
    st.write(f"*{en['text']}*")
    st.markdown("---")
else:
  st.error("Failed to load Surah list. Check your internet connection.")
