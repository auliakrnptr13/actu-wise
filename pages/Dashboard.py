import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="ActuWise - Dashboard",
    page_icon="🌿",
    layout="wide"
)

PRIMARY = "#C38B9B"      
SECONDARY = "#6E8E85"    
BACKGROUND = "#FFF2F4"   

# FIX CSS: Membungkus seluruh kode gaya ke dalam tag <style> agar tidak bocor ke layar luar
st.markdown(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp {{
    background-color: {BACKGROUND};
    font-family: 'Inter', sans-serif;
}}

/* Gaya Kartu Nilai Ringkasan Atas */
.metric-card {{
    background: white;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    box-shadow: 0px 8px 20px rgba(212, 165, 177, 0.15);
    border-top: 5px solid {PRIMARY};
}}

.metric-title {{
    color: {SECONDARY};
    font-size: 14px;
    font-weight: 600;
}}

.metric-value {{
    color: {PRIMARY};
    font-size: 26px;
    font-weight: 700;
    margin-top: 5px;
}}

/* Gaya Panel Navigasi Kartu (Seperti Gambar Ekspektasi Nomor 2) */
.nav-card {{
    background: white;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.05);
    border-top: 4px solid #9CC2BA;
    margin-bottom: 15px;
}}
.nav-card-title {{
    color: #4A5568;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
}}
.nav-card-desc {{
    color: #A0AEC0;
    font-size: 13px;
    margin-bottom: 15px;
}}
</style>
""", unsafe_allow_html=True)

# HEADER UTAMA DENGAN ICON (BEBAS EMOJI MENTAH)
st.markdown(f"""
<h1 style='color:{PRIMARY}; font-weight:700;'>
    <i class="fa-solid fa-chart-pie"></i> Dashboard Overview
</h1>
""", unsafe_allow_html=True)
st.caption("Wise Decisions for Your Financial Future")
st.markdown("---")

# KARTU INDIKATOR ATAS
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("<div class='metric-card'><div class='metric-title'><i class='fa-solid fa-wallet'></i> Premi Estimasi</div><div class='metric-value'>Rp 0</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card' style='border-top-color:{SECONDARY};'><div class='metric-title'><i class='fa-solid fa-chart-line'></i> Mortalitas (qx)</div><div class='metric-value'>0.0000</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-card'><div class='metric-title'><i class='fa-solid fa-heart-pulse'></i> Life Expectancy</div><div class='metric-value'>80 Tahun</div></div>", unsafe_allow_html=True)
with c4:
    st.markdown(f"<div class='metric-card' style='border-top-color:{SECONDARY};'><div class='metric-title'><i class='fa-solid fa-shield-halved'></i> Insurance Gap</div><div class='metric-value'>Rp 0</div></div>", unsafe_allow_html=True)

st.write("")

# GRAFIK TREND MORTALITAS
st.markdown(f"<h3 style='color:{PRIMARY}; margin-top:20px;'><i class='fa-solid fa-chart-area'></i> Mortality Trend</h3>", unsafe_allow_html=True)
usia = [20, 30, 40, 50, 60, 70, 80]
qx = [0.002, 0.003, 0.005, 0.009, 0.016, 0.042, 0.105]

fig = go.Figure()
fig.add_trace(go.Scatter(x=usia, y=qx, mode="lines+markers", name="qx", line=dict(color=PRIMARY, width=3), marker=dict(color=SECONDARY, size=8)))
fig.update_layout(title="Kurva Mortalitas", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor="white")
st.plotly_chart(fig, use_container_width=True)

# PANEL NAVIGASI INTERAKTIF BERBENTUK KARTU (Sesuai Gambar Nomor 2)
st.markdown(f"<h3 style='color:{PRIMARY}; margin-top:20px;'><i class='fa-solid fa-layer-group'></i> Panel Navigasi Interaktif</h3>", unsafe_allow_html=True)

grid_nav = st.columns(3)

with grid_nav[0]:
    st.markdown("<div class='nav-card'><div class='nav-card-title'>Kalkulator Premi</div><div class='nav-card-desc'>Perhitungan Tarif Kontribusi Asuransi Jiwa</div></div>", unsafe_allow_html=True)
    st.page_link("pages/Premi.py", label="Buka Kalkulator Premi", use_container_width=True)

with grid_nav[1]:
    st.markdown("<div class='nav-card' style='border-top-color:#D4A5B1;'><div class='nav-card-title'>Life Expectancy</div><div class='nav-card-desc'>Analisis Angka Harapan Sisa Usia Komorbid</div></div>", unsafe_allow_html=True)
    st.page_link("pages/Life_Expectancy.py", label="Buka Life Expectancy", use_container_width=True)

with grid_nav[2]:
    st.markdown("<div class='nav-card'><div class='nav-card-title'>Insurance Gap</div><div class='nav-card-desc'>Analisis Celah Defisit Proteksi Finansial</div></div>", unsafe_allow_html=True)
    st.page_link("pages/Insurance_Gap.py", label="Buka Insurance Gap", use_container_width=True)

st.markdown("---")
st.caption("© 2026 ActuWise • Wise Decisions for Your Financial Future")
