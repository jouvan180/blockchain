import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="CV Digital Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# 2. SIDEBAR UNTUK INPUT DATA
# ==========================================
st.sidebar.title("⚙️ Pengaturan Profil")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

# Nama
nama = st.sidebar.text_input(
    "👤 Nama Lengkap",
    "Jouvan Labib"
)

# NIM
nim = st.sidebar.text_input(
    "🆔 NIM",
    "2530801089"
)

# Jurusan
jurusan = st.sidebar.selectbox(
    "🎓 Jurusan",
    [
        "Informatika",
        "Sistem Informasi",
        "Teknik Komputer"
    ]
)

# Deskripsi / Bio
deskripsi = st.sidebar.text_area(
    "📝 Deskripsi Singkat (Bio)",
    "Saya adalah mahasiswa Informatika yang tertarik dengan dunia teknologi, pemrograman, pengembangan aplikasi, dan data science."
)

# Upload Foto
foto_profil = st.sidebar.file_uploader(
    "📷 Unggah Foto Profil (Opsional)",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# 3. PENGALAMAN ORGANISASI
# ==========================================
pengalaman_organisasi = st.sidebar.text_area(
    "🏢 Pengalaman Organisasi",
    "Contoh: Anggota OSIS dan mengikuti kegiatan organisasi sekolah."
)

# ==========================================
# 4. CHECKBOX MAGANG / SERTIFIKASI
# ==========================================
punya_pengalaman = st.sidebar.checkbox(
    "📜 Punya Pengalaman Magang/Sertifikasi?"
)

if punya_pengalaman:
    detail_pengalaman = st.sidebar.text_area(
        "📋 Detail Magang/Sertifikasi",
        "Contoh: Mengikuti pelatihan atau magang di bidang teknologi informasi."
    )
else:
    detail_pengalaman = ""

# ==========================================
# 5. PENGATURAN SKILL
# ==========================================
st.sidebar.markdown("---")
st.sidebar.subheader("🛠️ Atur Kemahiran Skill")

skill_python = st.sidebar.slider(
    "🐍 Python",
    0,
    100,
    80
)

skill_web = st.sidebar.slider(
    "🌐 Web Development",
    0,
    100,
    60
)

skill_db = st.sidebar.slider(
    "🗄️ Database",
    0,
    100,
    70
)

# ==========================================
# 6. AREA UTAMA
# ==========================================
st.title("🎓 Curriculum Vitae Digital")

st.markdown("---")

# Membuat 2 kolom
kolom_kiri, kolom_kanan = st.columns([2, 1])

# ==========================================
# KOLOM KIRI
# ==========================================
with kolom_kiri:

    st.header(nama)

    st.subheader(
        f"🎓 {jurusan} | 🆔 NIM: {nim}"
    )

    st.write(deskripsi)


# ==========================================
# KOLOM KANAN
# ==========================================
with kolom_kanan:

    if foto_profil is not None:
        st.image(
            foto_profil,
            width=200,
            caption="📷 Foto Profil"
        )

    else:
        st.image(
            "foto_profil.jpeg",
            width=200,
            caption="📷 Jouvan Labib"
        )

# ==========================================
# 7. PENGALAMAN ORGANISASI
# ==========================================
st.markdown("---")

st.markdown("### 🏢 Pengalaman Organisasi")

if pengalaman_organisasi:

    st.write(pengalaman_organisasi)

else:

    st.info(
        "anggota OSIS dan mengikuti kegiatan sekolah."
    )


# ==========================================
# 8. MAGANG / SERTIFIKASI
# ==========================================
st.markdown("---")

st.markdown("### 📜 Magang / Sertifikasi")

if punya_pengalaman:

    st.success(
        "✅ Memiliki pengalaman magang/sertifikasi"
    )

    st.info(
        detail_pengalaman
    )

else:

    st.info(
        "Belum memiliki pengalaman magang/sertifikasi."
    )


# ==========================================
# 9. KEAHLIAN TEKNIS
# ==========================================
st.markdown("---")

st.markdown("### 🛠️ Keahlian Teknis")

# Python
st.write(
    f"🐍 **Python — {skill_python}%**"
)

st.progress(skill_python)

# Web Development
st.write(
    f"🌐 **Web Development (HTML/CSS) — {skill_web}%**"
)

st.progress(skill_web)

# Database
st.write(
    f"🗄️ **Database (SQL) — {skill_db}%**"
)

st.progress(skill_db)


# ==========================================
# 10. KONTAK
# ==========================================
st.markdown("---")

st.markdown("### 📬 Hubungi Saya")

with st.expander("👆 Klik untuk melihat detail kontak"):

    # Membuat nama menjadi format tanpa spasi
    nama_user = nama.lower().replace(" ", "")

    st.write(
        f"📧 Email: {nama_user}@mahasiswa.univ.ac.id"
    )

    st.write(
        f"🔗 LinkedIn: linkedin.com/in/{nama_user}"
    )

    st.write(
        f"🐙 GitHub: github.com/{nama_user}"
    )


# ==========================================
# 11. DOWNLOAD DATA CV
# ==========================================
st.markdown("---")

st.markdown("### 📥 Download Data CV")

# Data yang akan dimasukkan ke file
data_cv = f"""Nama: {nama}
NIM: {nim}
Jurusan: {jurusan}
"""

# Tombol download
st.download_button(
    label="📥 Download Data CV",
    data=data_cv,
    file_name="cv_jouvan_labib.txt",
    mime="text/plain"
)