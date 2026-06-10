import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ActuWise - Actuarial Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="auto"
)

# 🎨 INJEKSI GAYA DAN THEME UTAMA PLATFORM
st.markdown("<style>html, body, [data-testid='stAppViewContainer'] { background-color: #FFF2F4 !important; font-family: 'Inter', sans-serif; }</style>", unsafe_allow_html=True)
st.markdown("<style>[data-testid='stSidebar'] { background-color: #FFFFFF !important; border-right: 1px solid #FAD6DC; }</style>", unsafe_allow_html=True)
st.markdown("<style>.stMetric { background-color: #FFFFFF !important; padding: 1.2rem !important; border-radius: 16px !important; border: 1px solid #FAD6DC !important; box-shadow: 0px 4px 12px rgba(212, 165, 177, 0.1); }</style>", unsafe_allow_html=True)

# Menyembunyikan navigasi bawaan Streamlit agar tampilan sidebar kustom kita bekerja sempurna
st.markdown("<style>[data-testid='stSidebarNav'] { display: none !important; }</style>", unsafe_allow_html=True)

# Memuat pustaka ikon Font Awesome & mengatur gaya ikon sidebar di bagian atas
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    .sidebar-icon {
        color: #C38B9B; 
        margin-right: 10px;
        font-size: 16px;
        display: inline-block;
        width: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# FUNGSI RENDER SIDEBAR KUSTOM (Spasi & Indentasi Sudah Diperbaiki)
def render_sidebar():
    st.sidebar.markdown("<h2 style='color: #D4A5B1; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<hr style='margin-top:0; border-color:#FAD6DC;'>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: #8A8A8A; font-size:0.8rem; font-weight:600; text-transform:uppercase; margin-bottom:0.8rem;'>MENU NAVIGASI</p>", unsafe_allow_html=True)
    
    # Semua link halaman di bawah ini sekarang sudah masuk 4 spasi (aman & lurus)
    st.sidebar.page_link(
        "Home.py", 
        label=":has[.sidebar-icon]<span class='sidebar-icon'><i class='fa-solid fa-gauge-high'></i></span>Dashboard Utama"
    )

    st.sidebar.page_link(
        "pages/Premi.py", 
        label=":has[.sidebar-icon]<span class='sidebar-icon'><i class='fa-solid fa-calculator'></i></span>Kalkulator Premi"
    )

    st.sidebar.page_link(
        "pages/Mortalitas.py", 
        label=":has[.sidebar-icon]<span class='sidebar-icon'><i class='fa-solid fa-chart-line'></i></span>Analisis Mortalitas"
    )

    st.sidebar.page_link(
        "pages/Life_Expectancy.py", 
        label=":has[.sidebar-icon]<span class='sidebar-icon'><i class='fa-solid fa-hourglass-half'></i></span>Angka Harapan Hidup"
    )

    st.sidebar.page_link(
        "pages/Insurance_Gap.py", 
        label=":has[.sidebar-icon]<span class='sidebar-icon'><i class='fa-solid fa-shield-halved'></i></span>Analisis Celah Proteksi"
    )

    st.sidebar.page_link(
        "pages/About.py", 
        label=":has[.sidebar-icon]<span class='sidebar-icon'><i class='fa-solid fa-circle-info'></i></span>Tentang Aplikasi"
    )
    
    st.sidebar.markdown("<hr style='border-color:#FAD6DC; margin-top:3rem;'>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-size: 0.85rem; color: #8A8A8A; margin-bottom: 0;'>Platform Developer:</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-weight: 700; color: #D4A5B1; margin-top: 0; font-size: 1.1rem;'>by Aulia Kurnia Putri</p>", unsafe_allow_html=True)


# MENJALANKAN SIDEBAR DAN MAIN VIEW DASHBOARD
render_sidebar()

st.markdown("<h1 style='color: #D4A5B1; font-weight:700; margin-bottom:0;'>ActuWise Analytics</h1>", unsafe_allow_html=True)
st.write("**Wise Decisions for Your Financial Future**")
st.caption("Sistem Ringkasan Indikator Performa Utama & Manajemen Risiko Aktuaria")
st.markdown("<hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)

# CONTAINER METRIK UTAMA
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Total Premium Written", value="
