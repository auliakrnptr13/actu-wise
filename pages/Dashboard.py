import streamlit as st
import plotly.graph_objects as go

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="ActuWise",
    page_icon="🌿",
    layout="wide"
)

# Definisikan tema warna premium (Pink & Sage Green lembut sesuai screenshot kamu)
PRIMARY = "#C38B9B"      # Rose Gold / Pink Tua
SECONDARY = "#6E8E85"    # Sage Green Tua
CARD_BORDER = "#FAD6DC"  # Pink Muda Pembatas
BACKGROUND = "#FFF2F4"   # Latar belakang pink sangat soft

# INJEKSI CSS: Memasukkan Font Awesome untuk Ikon & Mengubah Desain agar Estetik
st.markdown(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp {{
    background-color: {BACKGROUND};
    font-family: 'Inter', sans-serif;
}}

/* Desain Kartu Indikator Utama */
.card {{
    background: white;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0px 8px 24px rgba(212, 165, 177, 0.15);
    border-top: 5px solid {PRIMARY};
    transition: transform 0.2s;
}}

.card:hover {{
    transform: translateY(-3px);
}}

.card-title {{
    color: {SECONDARY};
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 8px;
}}

.card-value {{
    color: {PRIMARY};
    font-size: 28px;
    font-weight: 700;
}}

/* Mempercantik tampilan st.page_link agar mirip tombol navigasi premium */
.stElementContainer button, [data-testid="stPageLink-FormSubmitButton"] {{
    background-color: white !important;
    border: 1px solid {CARD_BORDER} !important;
    border-radius: 12px !important;
    padding: 10px 15px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.02) !important;
}}
</style>
""", unsafe_allow_html=True)

# 2. HEADER UTAMA (Menggunakan Ikon Font Awesome, Bukan Emoji)
st.markdown(f"""
<h1 style='color:{PRIMARY}; font-weight:700;'>
    <i class="fa-solid fa-chart-pie"></i> Dashboard Overview
</h1>
""", unsafe_allow_html=True)

st.caption("Wise Decisions for Your Financial Future")
st.markdown("---")

# 3. KARTU INDIKATOR UTAMA
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='card'>
        <div class='card-title'><i class="fa-solid fa-wallet"></i> Premi Estimasi</div>
        <div class='card-value'>Rp 0</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='card' style='border-top-color: {SECONDARY};'>
        <div class='card-title'><i class="fa-solid fa-skull-crossbones"></i> Mortalitas (qx)</div>
        <div class='card-value'>0.0000</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='card'>
        <div class='card-title'><i class="fa-solid fa-heart-pulse"></i> Life Expectancy</div>
        <div class='card-value'>80 Tahun</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='card' style='border-top-color: {SECONDARY};'>
        <div class='card-title'><i class="fa-solid fa-shield-halved"></i> Insurance Gap</div>
        <div class='card-value'>Rp 0</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# 4. GRAFIK INTERAKTIF MORTALITAS
st.markdown(f"<h3 style='color:{PRIMARY};'><i class='fa-solid fa-chart-line'></i> Mortality Trend</h3>", unsafe_allow_html=True)

usia = [20, 30, 40, 50, 60, 70, 80]
qx = [0.002, 0.003, 0.005, 0.009, 0.016, 0.042, 0.105]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=usia,
        y=qx,
        mode="lines+markers",
        name="qx",
        line=dict(color=PRIMARY, width=3),
        marker=dict(color=SECONDARY, size=8)
    )
)

fig.update_layout(
    title="Kurva Mortalitas",
    font=dict(family="Inter, sans-serif"),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)

# 5. RINGKASAN SISTEM
st.markdown(f"<h3 style='color:{PRIMARY};'><i class='fa-solid fa-circle-info'></i> Ringkasan Sistem</h3>", unsafe_allow_html=True)
st.info(
    """ActuWise adalah platform aktuaria berbasis web yang membantu pengguna melakukan simulasi premi, 
    analisis mortalitas, life expectancy, dan insurance gap secara interaktif."""
)

st.write("")
st.write("")

# 6. PERBAIKAN QUICK ACCESS (MENYESUAIKAN NAMA FILE DI SCREENSHOT AGAR TIDAK ERROR)
st.markdown(f"<h3 style='color:{PRIMARY};'><i class='fa-solid fa-bolt'></i> Quick Access</h3>", unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.page_link(
        "pages/Premi.py",  # Diperbaiki dari "pages/2_Premi.py" sesuai nama di sidebar menu kamu
        label="Premium Calculator",
        icon="✨" # Menggunakan icon default bawaan streamlit yang netral
    )

with b:
    st.page_link(
        "pages/Mortalitas.py", # Diperbaiki dari "pages/3_Mortalitas.py"
        label="Mortality Analytics",
        icon="✨"
    )

with c:
    st.page_link(
        "pages/Insurance_Gap.py", # Diperbaiki dari "pages/5_Insurance_Gap.py"
        label="Insurance Gap Analysis",
        icon="✨"
    )

st.markdown("---")
st.caption("© 2026 ActuWise • Wise Decisions for Your Financial Future")
