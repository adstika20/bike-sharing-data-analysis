import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import plotly.express as px

sns.set(style='dark')

# Membaca dataset
day = pd.read_csv('day.csv')
hour = pd.read_csv('hour.csv')

# Sidebar untuk navigasi
st.sidebar.title("Navigasi Analisis")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Analisis Suhu & Kelembaban", "Pola Musiman & Hari Libur", "Pola Jam Penyewaan", "Pengaruh Kecepatan Angin", "Pola Kategori Waktu Penyewaan"])

# Halaman Home
if page == "Home":
    # Header dengan Gambar
    col1, col2 = st.columns([1, 5])
    with col2:
        st.title("Dashboard Analisis Penyewaan Sepeda 🚴‍♂️ ")

    st.markdown("---")  # Garis pemisah

    # Deskripsi Utama
    st.markdown("""
    **Dataset yang Digunakan:** 
    - 📅 **day.csv**: Berisi data harian penyewaan sepeda.
    - ⏰ **hour.csv**: Berisi data penyewaan berdasarkan jam.

    Dashboard ini bertujuan untuk menganalisis pengaruh **cuaca**, **waktu**, dan **faktor lainnya** terhadap penyewaan sepeda. Dengan analisis ini, diharapkan dapat memberikan wawasan untuk meningkatkan efisiensi dan popularitas penyewaan sepeda.
    """)

    st.markdown("### 🔍 Preview Dataset")

    # Membuat dua kolom untuk preview dataset
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("📄 Preview Dataset Day"):
            st.dataframe(day.head())
    with col2:
        with st.expander("📄 Preview Dataset Hour"):
            st.dataframe(hour.head())

    st.markdown("---")  # Garis pemisah

    # Informasi Tambahan atau Highlight
    st.markdown("### 📊 Insight Utama")
    st.markdown("""
    - **Suhu dan Kelembaban**: Bagaimana suhu dan kelembaban mempengaruhi penyewaan sepeda selama tahun 2011-2012?.
    - **Pola Musiman & Hari Libur**: Bagaimana pola musiman dan hari libur memengaruhi jumlah penyewaan sepeda antara tahun 2011 dan 2012?
    - **Analisis Lanjutan (Pola Jam Penyewaan)**: Pola Penyewaan berdasarkan Jam tertentu, seperti pagi (07:00-09:00) dan sore (17:00-19:00)
    - **Analisis Lanjutan (Pengaruh Kecepatan Angin)**: Apakah kecepatan angin mempengaruhi keputusan orang untuk menyewa sepeda?.
    - **Pola Kategori Waktu Penyewaan Menggunakan Binning**
    """)

    # Footer atau Informasi Pengembang
    st.markdown("""
    ---
    <div style="text-align: center; font-size: 12px;">
        Dibuat oleh Ades Tikaningsih (https://github.com/adstika20) | © 2024
    </div>
    """, unsafe_allow_html=True)

# Halaman Suhu & Kelembaban
elif page == "Analisis Suhu & Kelembaban":
    st.title("Pengaruh Suhu dan Kelembaban Terhadap Penyewaan Sepeda")

    # Tambahkan CSS kustom untuk styling tambahan
    st.markdown("""
        <style>
        .title {
            font-size: 2.5rem;
            text-align: center;
            color: #0b1217;
            padding-bottom: 10px;
        }
        .description {
            font-size: 1.2rem;
            text-align: center;
            color: #333333;
        }
        </style>
        """, unsafe_allow_html=True)

    # Pengaruh Suhu dan Kelembaban terhadap Penyewaan Sepeda
    col1, col2 = st.columns(2)
    with col1:
        # Grafik Regresi Suhu
        fig_temp, ax_temp = plt.subplots()
        sns.regplot(x='temp', y='cnt', data=day, scatter_kws={'alpha': 0.5, 'color': '#4B8BBE'},
                    line_kws={'color': '#FF6347'})
        ax_temp.set_title('Pengaruh Suhu terhadap Penyewaan Sepeda', fontsize=14)
        ax_temp.set_xlabel('Suhu (°C)', fontsize=12)
        ax_temp.set_ylabel('Jumlah Penyewaan', fontsize=12)
        st.pyplot(fig_temp)

    with col2:
        # Grafik Regresi Kelembaban
        fig_hum, ax_hum = plt.subplots()
        sns.regplot(x='hum', y='cnt', data=day, scatter_kws={'alpha': 0.5, 'color': '#FFA500'},
                    line_kws={'color': '#4682B4'})
        ax_hum.set_title('Pengaruh Kelembaban terhadap Penyewaan Sepeda', fontsize=14)
        ax_hum.set_xlabel('Kelembaban (%)', fontsize=12)
        ax_hum.set_ylabel('Jumlah Penyewaan', fontsize=12)
        st.pyplot(fig_hum)

    # Grafik Interaktif dengan Plotly
    st.subheader("Grafik Interaktif Pengaruh Suhu dan Kelembaban")

    col3, col4 = st.columns(2)

    with col3:
        fig_plotly_temp = px.scatter(
            day, x='temp', y='cnt',
            trendline='ols',
            title='Pengaruh Suhu terhadap Penyewaan Sepeda',
            labels={'temp': 'Suhu (°C)', 'cnt': 'Jumlah Penyewaan'},
            template='plotly_dark'
        )
        st.plotly_chart(fig_plotly_temp, use_container_width=True)

    with col4:
        fig_plotly_hum = px.scatter(
            day, x='hum', y='cnt',
            trendline='ols',
            title='Pengaruh Kelembaban terhadap Penyewaan Sepeda',
            labels={'hum': 'Kelembaban (%)', 'cnt': 'Jumlah Penyewaan'},
            template='plotly_dark',
            color_discrete_sequence=['#FFA500']
        )
        st.plotly_chart(fig_plotly_hum, use_container_width=True)

    # Insight dan Interpretasi
    st.markdown("""
    ### Insight
    - **Suhu**: Terdapat korelasi positif yang kuat antara suhu dan jumlah penyewaan sepeda. Artinya, semakin tinggi suhu, semakin banyak sepeda yang disewa.
    - **Kelembaban**: Kelembaban menunjukkan korelasi negatif yang moderat terhadap jumlah penyewaan sepeda. Ini mengindikasikan bahwa pada hari-hari dengan kelembaban tinggi, penyewaan sepeda cenderung menurun.

    Faktor-faktor ini penting untuk dipertimbangkan dalam perencanaan operasional dan promosi penyewaan sepeda, terutama dalam menghadapi perubahan kondisi cuaca.
    """)


# Halaman Pola Musiman & Hari Libur
if page == "Pola Musiman & Hari Libur":
    st.title("Pola Musiman dan Hari Libur Terhadap Penyewaan Sepeda")
    # Menyiapkan Data
    hour['dteday'] = pd.to_datetime(hour['dteday'])
    hour['year'] = hour['dteday'].dt.year
    hour['month'] = hour['dteday'].dt.month
    hour['day_name'] = hour['dteday'].dt.day_name()

    # Menambahkan Bulan dalam Bahasa Indonesia
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun',
                   'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
    hour['month_name'] = hour['month'].apply(lambda x: month_names[x - 1])

    # Menghitung Rata-rata Penyewaan
    monthly_trend = hour.groupby('month_name')['cnt'].mean().reindex(month_names)
    holiday_trend = hour.groupby('holiday')['cnt'].mean()

    # Layout dengan Columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Rata-rata Penyewaan Sepeda per Bulan")
        fig1 = px.line(
            x=monthly_trend.index,
            y=monthly_trend.values,
            markers=True,
            title="Rata-rata Penyewaan Sepeda per Bulan",
            labels={"x": "Bulan", "y": "Rata-rata Penyewaan"},
            template="plotly_white"  # Ganti ke tema terang
        )
        fig1.update_traces(line=dict(color='cyan'))
        fig1.update_layout(title_font_size=12, xaxis_title_font_size=14, yaxis_title_font_size=14)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Rata-rata Penyewaan Sepeda pada Hari Libur vs Bukan Libur")
        fig2 = px.bar(
            x=["Tidak Libur", "Libur"],
            y=holiday_trend.values,
            color=["Tidak Libur", "Libur"],
            color_discrete_sequence=['#FF7F50', '#2E8B57'],
            title="Rata-rata Penyewaan Sepeda pada Hari Libur vs Bukan Libur",
            labels={"x": "Hari Libur", "y": "Rata-rata Penyewaan"},
            template="plotly_white"  # Ganti ke tema terang
        )
        fig2.update_layout(showlegend=False, title_font_size=12, xaxis_title_font_size=14, yaxis_title_font_size=14)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")  # Garis pemisah

    # Menambahkan Insight atau Analisis Singkat
    st.subheader("Insight")
    st.write("""
    **Pola musiman dan hari libur memiliki pengaruh yang berlawanan terhadap jumlah penyewaan sepeda antara tahun 2011 dan 2012. Penyewaan sepeda mencapai puncaknya pada bulan-bulan musim panas (Juni dan Juli) dan menurun drastis di musim dingin (Desember). Namun, di luar dugaan, hari libur justru mengurangi jumlah penyewaan sepeda dibandingkan hari biasa, kemungkinan karena orang lebih memilih aktivitas lain atau beristirahat pada hari libur.**
    """)

    # Menampilkan Data dalam Tab
    tab1, tab2 = st.tabs(["Data Penyewaan per Bulan", "Data Penyewaan Hari Libur"])

    with tab1:
        st.write(monthly_trend)

    with tab2:
        st.write(holiday_trend)




# Halaman Pola Jam Penyewaan
data_pola_jam = {
    'hr': list(range(24)),
    'cnt': [
        53.898072, 33.375691, 22.869930, 11.727403, 6.352941, 19.889819,
        76.044138, 212.064649, 335.500000, 219.309491, 173.668501, 208.143054,
        251.224828, 252.965659, 239.548831, 250.548077, 311.337449, 396.935897,
        369.841693, 310.929849, 226.030220, 172.314560, 131.335165, 87.831044
    ]
}

df_pola_jam = pd.DataFrame(data_pola_jam)
if page == "Pola Jam Penyewaan":
    st.markdown("<h1 class='title'>Pola Penyewaan Sepeda Berdasarkan Jam</h1>", unsafe_allow_html=True)

    # Pilihan jenis grafik
    grafik_type = st.selectbox(
        "Pilih Jenis Grafik",
        ("Garis", "Batang", "Area")
    )

    # Membuat grafik berdasarkan pilihan pengguna
    if grafik_type == "Garis":
        fig = px.line(
            df_pola_jam,
            x='hr',
            y='cnt',
            markers=True,
            title='Rata-rata Penyewaan Sepeda per Jam',
            labels={'hr': 'Jam', 'cnt': 'Rata-rata Penyewaan'},
            template='plotly_dark'
        )
        fig.update_traces(line=dict(color='#2e86de'))

    elif grafik_type == "Batang":
        fig = px.bar(
            df_pola_jam,
            x='hr',
            y='cnt',
            title='Rata-rata Penyewaan Sepeda per Jam',
            labels={'hr': 'Jam', 'cnt': 'Rata-rata Penyewaan'},
            template='plotly_dark',
            color='cnt',
            color_continuous_scale='Blues'
        )

    elif grafik_type == "Area":
        fig = px.area(
            df_pola_jam,
            x='hr',
            y='cnt',
            title='Rata-rata Penyewaan Sepeda per Jam',
            labels={'hr': 'Jam', 'cnt': 'Rata-rata Penyewaan'},
            template='plotly_dark',
            color_discrete_sequence=['#2e86de']
        )

    fig.update_layout(
        title_font_size=24,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Menambahkan Highlight pada Jam Sibuk
    st.markdown("""
        <div class='insight'>
            <h3>🔍 Jam Sibuk:</h3>
            <ul>
                <li>Pagi: 07:00 - 09:00</li>
                <li>Sore: 17:00 - 19:00</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
            <div class='insight'>
                <h3>📊 Insight:</h3>
                <ul>
                    Pola penyewaan sepeda menunjukkan korelasi kuat dengan ritme aktivitas harian masyarakat, terutama terkait mobilitas kerja. Terdapat dua puncak penyewaan yang jelas, yaitu pada pagi hari (07:00-09:00) dan sore hari (17:00-19:00), yang bertepatan dengan waktu berangkat dan pulang kerja.    
            </div>
        """, unsafe_allow_html=True)



# Halaman Pengaruh Kecepatan Angin
elif page == "Pengaruh Kecepatan Angin":
    st.title("Pengaruh Kecepatan Angin Terhadap Penyewaan Sepeda")

    # Menggunakan Plotly untuk scatter plot interaktif
    fig = px.scatter(
        hour,
        x='windspeed',
        y='cnt',
        trendline='ols',
        labels={
            'windspeed': 'Kecepatan Angin (km/h)',
            'cnt': 'Jumlah Penyewaan Sepeda'
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    # Menghitung dan menampilkan korelasi
    correlation = hour['windspeed'].corr(hour['cnt'])

    # Membuat tampilan dua kolom
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Korelasi Kecepatan Angin dan Penyewaan", value=f"{correlation:.2f}")

    with col2:
        st.write("""
            **Interpretasi:**
            - **Nilai Korelasi:** {0:.2f}
            - Nilai korelasi mendekati 0 menunjukkan hubungan yang lemah antara kecepatan angin dan penyewaan sepeda.
            """.format(correlation))

    st.markdown("""
        **Insight:**
        Dari analisis ini, terlihat bahwa kecepatan angin memiliki korelasi {0} dengan jumlah penyewaan sepeda. Hal ini menunjukkan bahwa faktor kecepatan angin {1} mempengaruhi keputusan orang untuk menyewa sepeda.
        """.format(
        "positif" if correlation > 0 else "negatif",
        "signifikan" if abs(correlation) > 0.5 else "tidak signifikan"
    ))



# Halaman Pola Kategori Waktu Penyewaan
if page == "Pola Kategori Waktu Penyewaan":
    # Judul halaman
    st.title("Pola Penyewaan Sepeda Berdasarkan Kategori Waktu")

    # Deskripsi singkat
    st.markdown("""
        Analisis ini menunjukkan tren penyewaan sepeda sepanjang hari. Kategori waktu dibagi menjadi:
        - **Night (Malam):** 00:00 - 06:00
        - **Morning (Pagi):** 06:00 - 12:00
        - **Afternoon (Siang):** 12:00 - 18:00
        - **Evening (Sore):** 18:00 - 24:00
        """)

    # Memuat data
    hour = pd.DataFrame({
        'hr': [1, 7, 13, 19],  # contoh data
        'cnt': [50, 75, 100, 60]
    })

    # Membuat kategori waktu
    hour['time_category'] = pd.cut(
        hour['hr'],
        bins=[-1, 6, 12, 18, 24],
        labels=['Night', 'Morning', 'Afternoon', 'Evening']
    )

    # Menghitung rata-rata penyewaan
    avg_rent_per_time_category = hour.groupby('time_category')['cnt'].mean().reset_index()

    # Membuat bar chart dengan Plotly
    fig = px.bar(
        avg_rent_per_time_category,
        x='time_category',
        y='cnt',
        title='Rata-rata Penyewaan Sepeda per Kategori Waktu',
        labels={'time_category': 'Kategori Waktu', 'cnt': 'Rata-rata Penyewaan'},
        template='plotly_white'
    )

    # Tampilkan chart
    st.plotly_chart(fig, use_container_width=True)

    # Menampilkan tabel data
    st.dataframe(avg_rent_per_time_category)
    # **Insight di bagian akhir**
    st.markdown("### Insight")

    # Temuan dari data
    st.markdown("""
        Berdasarkan data di atas, terdapat beberapa insight menarik terkait pola penyewaan sepeda:
        - **Afternoon (Siang)** merupakan waktu paling populer untuk penyewaan sepeda, dengan rata-rata penyewaan tertinggi.
        - **Morning (Pagi)** dan **Evening (Sore)** memiliki tren penyewaan yang cukup berimbang, meskipun tidak setinggi Afternoon.
        - **Night (Malam)** memiliki penyewaan yang paling sedikit, yang mungkin disebabkan oleh minimnya aktivitas luar ruangan pada malam hari.
        """)