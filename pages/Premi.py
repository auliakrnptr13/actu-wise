import streamlit as st

st.set_page_config(
    page_title="Premium Calculator",
    page_icon="💰",
    layout="wide"
)

PRIMARY = "#0A3323"
SECONDARY = "#105666"
CARD = "#839958"
BACKGROUND = "#F7F4D5"
ACCENT = "#D3968C"

st.markdown(f"""
<style>

.stApp {{
    background-color:{BACKGROUND};
}}

.result-card {{
    background:white;
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}}

</style>
""", unsafe_allow_html=True)

st.markdown(
    f"<h1 style='color:{PRIMARY};'>💰 Premium Calculator</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Simulasi premi asuransi berdasarkan profil pengguna"
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    usia = st.number_input(
        "Usia",
        min_value=0,
        max_value=100,
        value=0
    )

    jenis_kelamin = st.selectbox(
        "Jenis Kelamin",
        ["Perempuan", "Laki-laki"]
    )

with col2:

    uang_pertanggungan = st.number_input(
        "Uang Pertanggungan (Rp)",
        min_value=0,
        value=0,
        step=10000000
    )

premi = 0

if usia > 0 and uang_pertanggungan > 0:

    premi = uang_pertanggungan * 0.005

    if usia > 40:
        premi *= 1.25

    if usia > 60:
        premi *= 1.50

    if jenis_kelamin == "Laki-laki":
        premi *= 1.10

premi_bulanan = premi / 12

st.markdown("## 📊 Hasil Simulasi")

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
        <div class='result-card'>
        <h3>Premi Tahunan</h3>
        <h2>Rp {premi:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class='result-card'>
        <h3>Premi Bulanan</h3>
        <h2>Rp {premi_bulanan:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.subheader("📌 Interpretasi")

if premi == 0:

    st.info(
        "Masukkan data terlebih dahulu untuk melakukan simulasi."
    )

elif premi < 5000000:

    st.success(
        "Premi relatif ringan."
    )

elif premi < 10000000:

    st.warning(
        "Premi berada pada kategori menengah."
    )

else:

    st.error(
        "Premi cukup tinggi, pertimbangkan evaluasi kebutuhan proteksi."
    )
    
st.markdown("<br><hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #6E8E85;'><i class='fa-solid fa-graduation-cap'></i> Simulasi Premi Manfaat Berjenjang</h3>", unsafe_allow_html=True)
st.caption("Masukkan semua parameter, tingkat bunga, dan nilai komutasi dari tabel mortalitasmu sendiri.")

col_params1, col_params2, col_params3 = st.columns(3)

with col_params1:
    usia_input = st.number_input("Usia Tertanggung", min_value=0, max_value=100, value=0, step=1)
    bunga_input = st.number_input("Tingkat Bunga", min_value=0, max_value=100, value=0, step=1)

with col_params2:
    manfaat_1 = st.number_input("Manfaat Periode Pertama", min_value=0, value=0, step=1000000)
    periode_1 = st.number_input("Periode Pertama (Tahun)", min_value=0, value=0, step=1)

with col_params3:
    manfaat_2 = st.number_input("Manfaat Periode Kedua / Seterusnya", min_value=0, value=0, step=1000000)

st.markdown("<p style='color: #C38B9B; font-weight: 600; margin-top: 10px;'>📊 Nilai Komutasi Tabel Mortalitas :</p>", unsafe_allow_html=True)

col_data1, col_data2, col_data3 = st.columns(3)

with col_data1:
    D_x = st.number_input("Komutasi Dₓ", min_value=0.0, value=0.0, format="%.0f")

with col_data2:
    M_x = st.number_input("Komutasi Mₓ", min_value=0.0, value=0.0, format="%.0f")

with col_data3:
    M_x_n = st.number_input(f"Komutasi Mₓ₊ₙ", min_value=0.0, value=0.0, format="%.0f")
    
# 3. Tombol Eksekusi Perhitungan
if st.button("🧮 Hitung Premi Bersih Tunggal", use_container_width=True):
    
    # Validasi agar nilai pembagi (D_x) tidak nol supaya tidak crash
    if D_x > 0:
        # Mengubah input bunga persen menjadi desimal
        i_desimal = bunga_input / 100
        
        # Menghitung faktor diskonto v berdasarkan bunga yang diinput sendiri
        v = 1 / (1 + i_desimal) if (1 + i_desimal) != 0 else 0
        
        # 📝 LOGIKA AKTUARIA UTAMA (Komutasi murni menggunakan D_x dan M_x yang kamu input)
        # Komponen 1: Asuransi Berjangka n Tahun
        premi_berjangka = manfaat_1 * ((M_x - M_x_n) / D_x)
        
        # Komponen 2: Asuransi Seumur Hidup Ditunda n Tahun
        premi_ditunda = manfaat_2 * (M_x_n / D_x)
        
        # Total Premi Bersih Tunggal
        total_premi_tunggal = premi_berjangka + premi_ditunda
    else:
        premi_berjangka = 0.0
        premi_ditunda = 0.0
        total_premi_tunggal = 0.0
        st.warning("⚠️ Mohon isi nilai D_x dengan angka yang lebih besar dari 0 untuk memulai perhitungan.")

    # 4. Tampilkan Hasil Secara Elegan
    if D_x > 0:
        st.markdown("""
        <style>
            .hasil-box {
                background-color: white;
                border-left: 5px solid #C38B9B;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
                margin-top: 15px;
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='hasil-box'>
            <h4 style='color: #C38B9B; margin-top:0;'>Hasil Perhitungan Aktuaria:</h4>
            <p style='margin-bottom:5px; color:#4A5568;'><b>Tingkat Bunga Efektif (i):</b> {bunga_input}% (v = {v:.6f})</p>
            <p style='margin-bottom:5px; color:#4A5568;'><b>Komponen Asuransi Berjangka):</b> Rp {premi_berjangka:,.2f}</p>
            <p style='margin-bottom:5px; color:#4A5568;'><b>Komponen Asuransi Ditunda :</b> Rp {premi_ditunda:,.2f}</p>
            <hr style='border-color:#FAD6DC; margin: 10px 0;'>
            <h3 style='color: #6E8E85; margin:0;'>Total Premi Bersih Tunggal: Rp {total_premi_tunggal:,.2f}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"💡 **Analisis Teoretis:** Perhitungan ini sepenuhnya dinamis menggunakan tingkat bunga suku bunga kustom {bunga_input}% dan nilai fungsi komutasi yang ditentukan langsung dari basis data mortalitas Anda.")

import pandas as pd
import streamlit as st

# 1. Siapkan data untuk tabel
data_ringkasan = {
    "Parameter": [
        "Usia Tertanggung",
        "Masa Manfaat Periode I",
        "Santunan Periode I",
        "Santunan Periode II (Seumur Hidup)",
        "Tingkat Bunga",
        "Premi Bersih Tunggal"
    ],
    "Nilai / Keterangan": [
        f"{usia_input} Tahun",
        f"{periode_1} Tahun (Usia {usia_input} s.d {usia_input + periode_1})",
        f"Rp {manfaat_1:,.0f}",
        f"Rp {manfaat_2:,.0f}",
        f"{bunga_input}%",
        f"Rp {total_premi_tunggal:,.2f}"  # Menampilkan hasil dengan 2 angka di belakang koma
    ]
}

# 2. Ubah menjadi DataFrame Pandas
df_ringkasan = pd.DataFrame(data_ringkasan)

# 3. Tampilkan di Streamlit dengan format yang menarik
st.markdown("### 📊 Ringkasan Parameter & Hasil Perhitungan")
st.dataframe(
    df_ringkasan, 
    use_container_width=True,  # Membuat tabel penuh sesuai lebar layar
    hide_index=True            # Menyembunyikan kolom angka indeks (0, 1, 2..) bawaan pandas
)
st.caption(
    "ActuWise • Wise Decisions for Your Financial Future"
)
