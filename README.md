# Interactive Dashboard for Bike Rental Analysis Using Streamlit

Proyek ini adalah sebuah dashboard interaktif untuk menganalisis data penyewaan sepeda menggunakan Streamlit dan beberapa library Python seperti `plotly` dan `statsmodels`.

## Persyaratan Sistem

Sebelum menjalankan aplikasi ini, pastikan sistem Anda memiliki persyaratan berikut:

- Python 3.8 atau yang lebih baru
- `pip` untuk mengelola paket Python

## Cara Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/adstika20/Submission-Data-Analyst-Penyewaan-Sepeda.git
cd Submission-Data-Analyst-Penyewaan-Sepeda
```

### 2️⃣ **Membuat Virtual Environment**  
Buat dan aktifkan lingkungan virtual untuk memastikan dependensi tidak bentrok:  
```bash
python -m venv env
```
#### Aktifkan lingkungan virtual:
```bash
.\env\Scripts\activate
```
### 3️⃣ Instal Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Jalankan Aplikasi Streamlit
```bash
streamlit run main.py
```
### 📊 Dataset
Berikut dua dataset yang digunakan dalam aplikasi ini:

- `day.csv`: Dataset penyewaan sepeda berdasarkan hari.
- `hour.csv`: Dataset penyewaan sepeda per jam.
**Catatan:** Pastikan kedua berkas CSV ini berada di direktori yang sama dengan `main.py` agar aplikasi dapat berjalan dengan baik.

### 📦 Library dan Teknologi yang Digunakan
- `streamlit`: Untuk membangun aplikasi web interaktif.
- `plotly`: Untuk visualisasi data.
- `pandas`: Untuk manipulasi data.
- `numpy`: Untuk operasi numerik.
- `statsmodels`: Untuk analisis statistik.
