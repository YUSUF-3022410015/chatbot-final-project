import streamlit as st
import google.generativeai as genai
import os

# --- KONFIGURASI ---
# Ganti dengan API Key milikmu
API_KEY = "AIzaSyDkIlqmLstQLhOzoI6b1iAmcUizjo_P4Gk" 

genai.configure(api_key=API_KEY)

# Parameter Kreatif: Mengatur "Kepribadian" Chatbot
system_instruction = (
    "Kamu adalah 'Yusuf AI', asisten bisnis cerdas untuk Toko Masyusuf. "
    "Tugasmu membantu pelanggan memilih beras terbaik (Rojo Lele, Rinjani, atau Ramos). "
    "Gaya bahasamu ramah, santai, dan solutif. "
    "Jika ditanya soal sistem informasi, kamu juga bisa menjawab dengan perspektif mahasiswa UISI."
)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    system_instruction=system_instruction
)

# --- UI STREAMLIT ---
st.set_page_config(page_title="Yusuf Business AI", page_icon="🌾")

st.title("🌾 Yusuf Business Assistant")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.markdown("### Info Pengembang")
    st.write("Nama: Yusuf Dede Yonaldy")
    st.write("Prodi: Sistem Informasi UISI")
    st.divider()
    st.write("Chatbot ini menggunakan model Gemini AI untuk membantu operasional Toko Masyusuf.")
    
st.caption("Final Project: AI Chatbot for Business & Academic")

# Memory Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan history chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Cari bagian ini di kode kamu dan bungkus dengan try-except
if prompt := st.chat_input("Ada yang bisa saya bantu?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Waduh, ada kendala teknis: {e}")