# Interactive Dashboard for Bike Rental Analysis Using Streamlit

🔍 Sebuah Dashboard interaktif untuk mengeksplorasi dan menganalisis tren penyewaan sepeda menggunakan **Python**, **Plotly**, dan **Streamlit**.  
Dirancang untuk menyajikan wawasan berbasis data dengan tampilan yang intuitif dan mudah digunakan.

---

## 1. Ringkasan Proyek

Proyek ini dibuat sebagai bagian dari proyek akhir analisis data. Mencakup:
- Proses lengkap analisis data dari awal hingga kesimpulan
- Pembuatan dasbor interaktif menggunakan **Streamlit**
- Visualisasi berbasis **Plotly** untuk menjawab pertanyaan bisnis yang relevan

---

## 2. Key Outcomes / Preview

Dasbor ini menyajikan:
- 📅 Analisis tren penyewaan berdasarkan hari dan jam  
- 🌦️ Perbandingan cuaca dengan pola penyewaan  
- 🧍‍♂️ Segmentasi berdasarkan tipe pengguna  
- 🔄 Fluktuasi penggunaan musiman dan harian

![Pratinjau Dashboard](https://github.com/adstika20/bike-sharing-data-analysis/blob/main/Preview%20Dashboard.png)

Try the live version 👉 [Buka Aplikasi](https://adstika20-submission-data-analyst-penyewaan-sepeda-main-2ljso0.streamlit.app/)

---

## 3. Struktur Proyek

```bash
Submission-Data-Analyst-Penyewaan-Sepeda/
│
├── data/
│   ├── day.csv
│   └── hour.csv
│
├── main.py                # Kode utama dashboard Streamlit
├── eda_notebook.ipynb     # Notebook 
├── requirements.txt       # Daftar dependensi
└── README.md              # Dokumentasi proyek
```

## 4. Installation & Setup

### Requirements
- Python ≥ 3.8
- pip (Python package installer)
- (Optional) virtualenv or conda for isolated environments

### Installation
```
# Clone the repo
git clone https://github.com/adstika20/Submission-Data-Analyst-Penyewaan-Sepeda.git
cd Submission-Data-Analyst-Penyewaan-Sepeda

# Create and activate virtual environment
python -m venv env
# Windows
.\env\Scripts\activate
# macOS/Linux
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard
streamlit run main.py
```
## 5. Dataset

Dataset yang digunakan dalam proyek ini berasal dari sumber berikut:

🔗 [Unduh Dataset - Google Drive](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)

Dataset terdiri atas dua file utama:

- `day.csv` — Data penyewaan sepeda **per hari**
- `hour.csv` — Data penyewaan sepeda **per jam**

## 🙌 Penutup
Proyek ini merupakan bagian dari proyek akhir pembelajaran sebagai analis data.
Menunjukkan kemampuan untuk:
- Menerjemahkan kebutuhan bisnis ke dalam pertanyaan analitis
- Mengolah data menjadi informasi yang mudah dipahami
- Membangun aplikasi berbasis data secara interaktif.
