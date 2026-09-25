# 🎓 Blockchain Explorer - Data Mahasiswa

## 1. Informasi Project

| Keterangan | Detail                    |
| ---------- | ------------------------- |
| Nama       | Jouvan Labib              |
| NIM        | 2530801089                |
| Prodi      | Informatika               |
| Kelas      | Informatika 2D            |
| Semester   | 3                        |
| Pertemuan  | 4                         |
| Tema       | Blockchain Data Mahasiswa |

## 2. Deskripsi

**Blockchain Explorer - Data Mahasiswa** adalah aplikasi Python dan Streamlit untuk menyimpan data mahasiswa ke dalam blockchain sederhana.

Data yang disimpan:

* NIM
* Nama Mahasiswa
* IPK
* Prestasi
* Jurusan
* Tahun Ajaran

## 3. Teknologi

* Python
* Streamlit
* SHA-256
* `hashlib`
* `time`
* `datetime`

## 4. Struktur Project

```text
ptmn4-blockchain-mahasiswa/
├── app.py
├── core.py
└── LAPORAN.md
```

`app.py` digunakan untuk tampilan dan input data.
`core.py` berisi class `Block` dan `Blockchain`.

## 5. Input dan Prestasi

Input utama pada `app.py`:

```python
nim = st.sidebar.text_input("NIM =")
Mahasiswa = st.sidebar.text_input("Nama Mahasiswa =")
ipk = st.sidebar.number_input(
    "IPK =", min_value=0.0,
    max_value=4.0, step=0.01,
    format="%.2f"
)
```

Prestasi ditentukan berdasarkan IPK:

```python
if ipk >= 3.5:
    prestasi = "Mahasiswa cumlaude 🎓"
elif ipk >= 3.0:
    prestasi = "Mahasiswa memuaskan 🌟"
elif ipk >= 2.5:
    prestasi = "Mahasiswa cukup memuaskan"
else:
    prestasi = "Mahasiswa kurang memuaskan 😞"
```

Data kemudian dibuat menjadi payload:

```python
data = (
    f"NIM: {nim} | Nama: {Mahasiswa} | "
    f"IPK: {ipk:.2f} | Prestasi: {prestasi} | "
    f"Jurusan: {jurusan} | Tahun Ajaran: {tahun_ajaran}"
)
```

## 6. Implementasi Blockchain

Class `Block` menyimpan:

```python
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
```

Hash dibuat menggunakan SHA-256:

```python
def calculate_hash(self):
    block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
    return hashlib.sha256(block_string.encode()).hexdigest()
```

Blockchain dimulai dengan Genesis Block:

```python
genesis_block = Block(
    0, time.time(), "Genesis Block", "0"
)
self.chain.append(genesis_block)
```

Block baru ditambahkan menggunakan hash block sebelumnya:

```python
def add_block(self, data):
    last_block = self.chain[-1]
    new_block = Block(
        len(self.chain),
        time.time(),
        data,
        last_block.hash
    )
    self.chain.append(new_block)
```

## 7. Validasi Blockchain

Validasi dilakukan dengan memeriksa hash dan `previous_hash`:

```python
if current_block.hash != current_block.calculate_hash():
    return False

if current_block.previous_hash != previous_block.hash:
    return False
```

Jika semua sesuai, hasilnya:

```python
return True
```

Pada aplikasi ditampilkan **Blockchain valid**.

## 8. Fitur Aplikasi

Aplikasi memiliki fitur:

* Tambah data mahasiswa.
* Penentuan prestasi berdasarkan IPK.
* Penyimpanan data ke blockchain.
* Menampilkan hash dan previous hash.
* Menampilkan waktu block.
* Validasi blockchain.
* Pencarian data berdasarkan NIM.

Pencarian dilakukan dengan:

```python
if cari_mahasiswa in block.data:
```

## 9. Pengujian

Contoh data:

```text
NIM          : 2530801089
Nama         : Jouvan Labib
IPK          : 3.50
Jurusan      : Teknik Informatika
Tahun Ajaran : 2024/2025
```

Hasil prestasi:

```text
Mahasiswa cumlaude 🎓
```

Data kemudian disimpan sebagai block dan dapat dicari kembali berdasarkan NIM.

## 10. Cara Menjalankan

```bash
streamlit run app.py
```

## 11. Kesimpulan

Project ini berhasil menerapkan konsep dasar blockchain menggunakan Python dan Streamlit. Data mahasiswa disimpan dalam block yang memiliki **index, timestamp, data, previous hash, dan hash**. SHA-256 digunakan untuk menghasilkan hash, sedangkan validasi dilakukan dengan memeriksa hash dan hubungan antar-block.
