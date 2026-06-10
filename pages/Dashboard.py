import streamlit as st

st.set_page_config(
    page_title="ActuWise - Security Gateway",
    page_icon="🌿",
    layout="wide"
)

# 🎨 INJEKSI CSS PREMIUM: Menggabungkan tema warna pink lembut dengan gaya kartu Tampilan Nomor 2
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [data-testid='stAppViewContainer'] {
        background-color: #FFF2F4 !important; /* Latar belakang pink soft dari gambar */
        font-family: 'Inter', sans-serif;
    }
    
    /* JUDUL BESAR GAYA TAMPILAN NOMOR 2 */
    .brand-title {
        color: #C38B9B;
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 5px;
    }
    .brand-subtitle {
        color: #8A8A8A;
        font-size: 16px;
        text-align: center;
        margin-bottom: 40px;
    }

    /* KARTU FORM LOGIN/REGISTER (Gaya Card View Tampilan Nomor 2) */
    .auth-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(212, 165, 177, 0.25);
        border-top: 6px solid #9CC2BA; /* Garis aksen atas seperti komponen hijau di Tampilan 2 */
        max-width: 550px;
        margin: 0 auto;
    }
    
    /* GAYA INPUTAN BARU (Bukan kotak hitam pekat lagi agar mudah dibaca dosen) */
    .stTextInput > div > div > input {
        background-color: #FAFAFA !important;
        border: 1px solid #E2E8F0 !important;
        color: #2D3748 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 1. JUDUL UTAMA (Mengikuti gaya huruf Tampilan Nomor 2, diubah menjadi "ActuWise")
st.markdown("<div class='brand-title'>ActuWise</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Wise Decisions for Your Financial Future</div>", unsafe_allow_html=True)

# 2. NAVIGASI TOMBOL PILIHAN DENGAN ICON (Mengubah tampilan tombol polos nomor 1 jadi berikon)
col_nav1, col_nav2 = st.columns([1, 1])

# Inisialisasi status form login/register
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = 'Login'

with col_nav1:
    # Menggunakan ikon kunci (key) untuk Login
    if st.button("🔑 Masuk (Login)", use_container_width=True):
        st.session_state.auth_mode = 'Login'

with col_nav2:
    # Menggunakan ikon pengguna baru (user-plus) untuk Register
    if st.button("📝 Daftar Akun (Register)", use_container_width=True):
        st.session_state.auth_mode = 'Register'

st.markdown("<br>", unsafe_allow_html=True)

# 3. KARTU DINAMIS (Wadah inputan dengan gaya Tampilan Nomor 2)
if st.session_state.auth_mode == 'Login':
    st.markdown("""
    <div class='auth-card'>
        <h3 style='color: #C38B9B; margin-top:0; text-align:center;'>
            <i class="fa-solid fa-right-to-bracket"></i> Gerbang Masuk Platform
        </h3>
        <p style='color: #718096; text-align:center; font-size:14px; margin-bottom:25px;'>
            Silakan masukkan kredensial yang terdaftar untuk mengakses berkas aktuaria.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input field diletakkan di bawah kartu secara rapi
    email = st.text_input("Alamat Email / Username")
    password = st.text_input("Password", type="password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔓 Buka Dashboard ActuWise", use_container_width=True):
        st.success("Akses diberikan! Membuka berkas...")
        
else:
    # Tampilan Form Pendaftaran Akun Baru
    st.markdown("""
    <div class='auth-card' style='border-top-color: #D4A5B1;'>
        <h3 style='color: #C38B9B; margin-top:0; text-align:center;'>
            <i class="fa-solid fa-user-plus"></i> Registrasi Akun Baru
        </h3>
        <p style='color: #718096; text-align:center; font-size:14px; margin-bottom:25px;'>
            Isi formulir di bawah ini untuk membuat otoritas akses sistem baru.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    email_baru = st.text_input("Alamat Email Baru")
    username_baru = st.text_input("Username Baru")
    password_baru = st.text_input("Password Baru", type="password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Daftarkan Akun Otoritas", use_container_width=True):
        st.success("Akun berhasil dibuat! Silakan klik menu Masuk (Login) di atas.")
