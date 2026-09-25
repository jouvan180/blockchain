import streamlit as st
from core import Blockchain

st.set_page_config(page_title="Blockchain Eksplorer - Data Mahasiswa", page_icon="🎓", layout="wide")

st.title("🎓 Blockchain Eksplorer - Data Mahasiswa")

if "blockchain" not in st.session_state:
    st.session_state["blockchain"] = Blockchain()

st.sidebar.header("➕ Tambah Data Mahasiswa")

nim = st.sidebar.text_input("NIM =")
Mahasiswa = st.sidebar.text_input("Nama Mahasiswa =")
ipk = st.sidebar.number_input("IPK =", min_value=0.0, max_value=4.0, step=0.01, format="%.2f")
jurusan = st.sidebar.selectbox("Jurusan =", ["Teknik Informatika", "Sistem Informasi", "Teknik Elektro", "Teknik Mesin","Teknik Sipil", 
                                             "Arsitektur", "Desain Komunikasi Visual", "Manajemen", "Akuntansi", "Psikologi", "Hukum", 
                                             "Kedokteran", "Farmasi", "Ilmu Komunikasi", "Ilmu Politik", "Sastra Inggris", "Sastra Jepang", 
                                             "Sastra Korea", "Sastra Perancis", "Sastra Jerman", "Sastra Arab"])
if ipk >= 3.5:
    prestasi="Mahasiswa cumlaude 🎓"
elif ipk >= 3.0:
    prestasi="Mahasiswa memuaskan 🌟"
elif ipk >= 2.5:
    prestasi="Mahasiswa cukup memuaskan"
else:
    prestasi="Mahasiswa kurang memuaskan 😞"
tahun_ajaran = st.sidebar.selectbox("Tahun Ajaran =", ["2020/2021", "2021/2022", "2022/2023", "2023/2024", "2024/2025"])
if st.sidebar.button("Tambahkan Data"):
    if nim and Mahasiswa and jurusan and tahun_ajaran:
        data = (
            f"NIM: {nim} | Nama: {Mahasiswa} | "
            f"IPK: {ipk:.2f} | Prestasi: {prestasi} | "
            f"Jurusan: {jurusan} | Tahun Ajaran: {tahun_ajaran}"
        )
        

        st.session_state.blockchain.add_block(data)
        st.success("Data berhasil ditambahkan ke blockchain!")
    else:
        st.error("Harap isi semua field sebelum menambahkan data.")


st.subheader("📜 Riwayat Data Mahasiswa")

is_chain_valid = st.session_state.blockchain.is_chain_valid()
if is_chain_valid:
    st.success("✅ Blockchain valid") 
else:
    st.error("❌ Blockchain tidak valid")

for block in st.session_state.blockchain.chain[1:]:
    with st.expander(f"Data {block.index} | Hash: {block.hash[:15]}..."):
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Data Payload:**")
            st.info(block.data)
            st.write(f"**Waktu:** {block.timestamp_readable}")

        with col2:
            st.write("**Kriptografi:**")
            st.write("**Hash saat ini:**")
            st.code(block.hash, language="python")
            st.write("**Hash sebelumnya (pointer):**")
            st.code(block.previous_hash, language="python")

cari_mahasiswa = st.text_input("Cari Data Mahasiswa (NIM):")
if cari_mahasiswa:
    found = False

    for block in st.session_state.blockchain.chain[1:]:
        if cari_mahasiswa in block.data:
            st.success(f"Data ditemukan di blok {block.index}:")
            st.info(block.data)
            found = True
            break

    else:
        st.warning("Data tidak ditemukan di blockchain.")
