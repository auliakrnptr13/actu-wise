import streamlit as st

st.set_page_config(
    page_title="Premium Calculator - ActuWise",
    page_icon="🌿",
    layout="wide"
)

# Definisi Palet Warna Premium ActuWise (Soft Pink & Sage Green)
PRIMARY = "#C38B9B"      # Soft Pink Utama
SECONDARY = "#6E8E85"    # Sage Green Pendukung
BACKGROUND = "#FFF2F4"   # Latar Belakang Soft Pink

# 1. Injeksi Desain Tema Visual Kustom
st.markdown(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700&display=swap');

html, body, [data-testid='stAppViewContainer'] {{
    background-color: {BACKGROUND} !important;
    font-family: 'Inter', sans-serif;
}}

/* Gaya Kartu Hasil Desain Minimalis */
.result-card {{
    background: white;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(212, 165, 177, 0.15);
    border-top: 4px solid {PRIMARY};
}}

.result-card h3 {{
    color: {SECONDARY};
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 8px;
}}

.result-card h2 {{
    color: #2D3748;
    font-size: 28px;
    font-weight: 700;
    margin: 0;
}}

.section-title {{
    color: {PRIMARY};
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 5px;
}}
</style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown(f"<h1 style='color:{PRIMARY}; font-weight:700;'><i class='fa-solid fa-calculator'></i> Kalkulator Premi Manfaat Berjenjang</h1>", unsafe_allow_html=True)
st.caption("Simulasi perhitungan Premi Bersih Tunggal dan Premi Berkala berdasarkan parameter kustom serta fungsi komutasi.")
st.markdown("<hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)


# =========================================================================
# STEP 1: INPUT PARAMETER UTAMA SOAL
# =========================================================================
st.markdown(f"<h3 class='section-title'><i class='fa-solid fa-sliders'></i> 1. Parameter Profil & Ketentuan Manfaat</h3>", unsafe_allow_html=True)

col_params1, col_params2, col_params3 = st.columns(3)

with col_params1:
    usia_input = st.number_input("Usia Tertanggung (x)", min_value=0, max_value=100, value=30, step=1)
    bunga_input = st.number_input("Tingkat Bunga (i) dalam %", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

with col_params2:
    manfaat_1 = st.number_input("Manfaat Periode Pertama (Rp)", min_value=0, value=0, step=10000000)
    periode_1 = st.number_input("Periode Pertama (Tahun)", min_value=1, value=10, step=1)

with col_params3:
    manfaat_2 = st.number_input("Manfaat Periode Kedua / Seterusnya (Rp)", min_value=0, value=0, step=10000000)


# =========================================================================
# STEP 2: INPUT NILAI KOMUTASI TABEL MORTALITAS
# =========================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"<h3 class='section-title'><i class='fa-solid fa-table-list'></i> 2. Nilai Fungsi Komutasi Aktuaria</h3>", unsafe_allow_html=True)
st.caption("Masukkan ekstrak nilai komutasi dari tabel mortalitas yang Anda gunakan agar kalkulasi berjalan akurat.")

col_data1, col_data2, col_data3 = st.columns(3)

with col_data1:
    D_x = st.number_input("Nilai D_x (Sesuai Usia x)", min_value=0.0, value=0.0, format="%.4f")

with col_data2:
    M_x = st.number_input("Nilai M_x (Sesuai Usia x)", min_value=0.0, value=0.0, format="%.4f")

with col_data3:
    M_x_n = st.number_input(f"Nilai M_(x+n) (Sesuai Usia {usia_input + periode_1})", min_value=0.0, value=0.0, format="%.4f")

st.markdown("<br>", unsafe_allow_html=True)


# =========================================================================
# STEP 3: PROSES EKSEKUSI LOGIKA & TAMPILAN HASIL UTAMA
# =========================================================================
if st.button("Hitung Estimasi Nilai Premi", use_container_width=True):
    
    if D_x > 0:
        # Konversi bunga persen ke desimal untuk faktor diskonto
        i_desimal = bunga_input / 100
        v = 1 / (1 + i_desimal) if (1 + i_desimal) != 0 else 0
        
        # LOGIKA PERHITUNGAN AKTUARIA BERBASIS KOMUTASI PURE
        # Komponen 1: Asuransi Jiwa Berjangka n-Tahun
        premi_berjangka = manfaat_1 * ((M_x - M_x_n) / D_x)
        
        # Komponen 2: Asuransi Jiwa Seumur Hidup Ditunda n-Tahun
        premi_ditunda = manfaat_2 * (M_x_n / D_x)
        
        # Total Premi Bersih Tunggal (Net Single Premium)
        total_premi_tunggal = premi_berjangka + premi_ditunda
        
        # Estimasi Premi Berkala (Asumsi dasar penyebaran beban nilai amortisasi)
        premi_tahunan = total_premi_tunggal * 0.075  
        premi_bulanan = premi_tahunan / 12
        
        # Menampilkan Dashboard Hasil Panel Kartu Minimalis
        st.markdown(f"<br><h3 class='section-title'><i class='fa-solid fa-square-poll-vertical'></i> 3. Hasil Analisis Keuangan Ringkas</h3>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown(f"""
                <div class='result-card'>
                    <h3>Premi Bersih Tunggal (A_x)</h3>
                    <h2>Rp {total_premi_tunggal:,.0f}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.markdown(f"""
                <div class='result-card' style='border-top-color: {SECONDARY};'>
                    <h3>Estimasi Premi Tahunan</h3>
                    <h2>Rp {premi_tahunan:,.0f}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with c3:
            st.markdown(f"""
                <div class='result-card'>
                    <h3>Estimasi Premi Bulanan</h3>
                    <h2>Rp {premi_bulanan:,.0f}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        # Segment Interpretasi & Teori Pendukung Akademis
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Interpretasi & Hasil Evaluasi")
        
        if total_premi_tunggal < 5000000:
            st.success("Tingkat eksposur risiko dana relatif aman dan nilai kontribusi premi tergolong ringan.")
        elif total_premi_tunggal < 15000000:
            st.warning("Nilai kontribusi berada dalam taraf standar rata-rata perhitungan cadangan kecukupan.")
        else:
            st.error("Kalkulasi beban premi tinggi, direkomendasikan melakukan re-evaluasi target tingkat suku bunga.")
            
        st.info(f"Faktor diskonto efektif yang terbentuk dari suku bunga kustom adalah v = {v:.6f}. Formulasi ini secara otomatis membagi komponen kewajiban asuransi jangka pendek berjangka {periode_1} tahun dan proteksi seumur hidup tertunda tanpa mencampur rumus mentah non-aktuaria.")
        
    else:
        st.error("Sistem tidak dapat melakukan pembagian. Mohon isi nilai D_x dengan angka yang valid (lebih besar dari 0).")

st.markdown("<br><hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)
st.caption("ActuWise • Wise Decisions for Your Financial Future")
