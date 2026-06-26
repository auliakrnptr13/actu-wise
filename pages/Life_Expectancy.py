import streamlit as st

st.set_page_config(
    page_title="Angka Harapan Hidup - ActuWise", 
    layout="wide"
)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [data-testid='stAppViewContainer'] {
        background-color: #FFF2F4 !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* GAYA KARTU HASIL */
    .result-box {
        background-color: white; 
        padding: 25px; 
        border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(212, 165, 177, 0.15);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #C38B9B;'><i class='fa-solid fa-heart-pulse'></i> Analisis Angka Harapan Hidup</h2>", unsafe_allow_html=True)
st.markdown("<hr style='border-color:#FAD6DC; margin-bottom: 25px;'>", unsafe_allow_html=True)

st.write("##### Parameter Perhitungan Aktuaria (Faktor Risiko Kesehatan):")

usia_input = st.number_input("Masukkan Usia Responden Saat Ini", value=22, min_value=0, max_value=90)

status_kesehatan = st.radio(
    "Bagaimana kondisi riwayat medis responden saat ini?", 
    ["Kondisi Sehat / Prima (Standard Risk)", "Memiliki Riwayat Penyakit"]
)

batas_normal = 78.0

if status_kesehatan == "Memiliki Riwayat Penyakit":
    jenis_penyakit = st.selectbox(
        "Pilih Kategori Penyakit untuk Penyesuaian Koefisien Morbiditas:", 
        ["Penyakit Ringan / Terkontrol (Hipertensi, Asam Urat, dll)", 
         "Penyakit Kronis Berat (Diabetes Melitus, Jantung, Ginjal, dll)"]
    )
    
    if "Ringan" in jenis_penyakit:
        sisa_harapan = (batas_normal - usia_input) - 5.0  # Penyakit ringan mengurangi 5 tahun
        keterangan = "Angka harapan hidup mengalami penyesuaian berkurang 5 tahun karena faktor morbiditas risiko sedang."
        warna_sisi = "#E5BCC6"  # Warna aksen pink sedang
    else:
        sisa_harapan = (batas_normal - usia_input) - 12.0 # Penyakit berat mengurangi 12 tahun
        keterangan = "Peringatan: Angka harapan hidup berkurang 12 tahun akibat paparan risiko komorbiditas tinggi."
        warna_sisi = "#D4A5B1"  # Warna aksen rose gold pekat
else:
    sisa_harapan = batas_normal - usia_input
    keterangan = "Kondisi tubuh prima (Standard Risk). Proyeksi angka harapan hidup berjalan optimal secara normal."
    warna_sisi = "#9CC2BA"  # Warna aksen hijau sage soft

sisa_harapan = float(max(0.0, sisa_harapan))

st.markdown(f"""
<div class='result-box' style='border-left: 8px solid {warna_sisi};'>
    <h4 style='color: #4A5568; margin-top:0;'><i class="fa-solid fa-hourglass-half"></i> Proyeksi Sisa Umur Produktif</h4>
    <h1 style='color: #C38B9B; margin: 10px 0;'>{sisa_harapan:.1f} Tahun Lagi</h1>
    <p style='margin:0; color:#6E8E85; font-weight:500;'><i class="fa-solid fa-circle-exclamation"></i> Analisis: {keterangan}</p>
</div>
""", unsafe_allow_html=True)
