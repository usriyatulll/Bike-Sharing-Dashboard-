# Bike Sharing Data Analysis Dashboard

## Deskripsi
Dashboard ini merupakan aplikasi Streamlit yang dirancang untuk menganalisis data berbagi sepeda dari dataset Bike Sharing. Aplikasi ini menampilkan visualisasi data yang membantu dalam memahami pengaruh cuaca terhadap penggunaan sepeda dan tren penggunaan sepeda berdasarkan waktu.

## Daftar Isi
1. [Persyaratan](#persyaratan)
2. [Instalasi](#instalasi)
3. [Menjalankan Dashboard](#menjalankan-dashboard)
4. [Penjelasan Proyek](#penjelasan-proyek)
5. [Link Dashboard](#link-dashboard)

## Persyaratan
- Python 3.8 atau lebih tinggi
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Instalasi
1. **Clone repositori ini**:
    ```bash
    git clone https://github.com/usroyatulll/Bike-Sharing-Dashboard-.git
    cd repository
    ```

2. **Buat dan aktifkan lingkungan virtual**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3. **Instal dependensi**:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Dashboard
1. Aktifkan lingkungan virtual (jika belum):
    ```bash
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

2. Jalankan aplikasi Streamlit:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

3. Akses dashboard di browser Anda melalui [http://localhost:8501](http://localhost:8501).

## Penjelasan Proyek
- **Visualisasi 1**: Pengaruh Cuaca terhadap Penggunaan Sepeda
    - Visualisasi ini menampilkan scatter plot yang menunjukkan hubungan antara suhu dan jumlah penggunaan sepeda dengan warna yang menunjukkan kondisi cuaca.

- **Visualisasi 2**: Tren Penggunaan Sepeda Berdasarkan Waktu
    - Visualisasi ini mencakup dua plot garis: satu untuk tren penggunaan sepeda per jam dan satu lagi untuk tren per hari, dengan warna yang menunjukkan hari dalam minggu dan musim.

- **Analisis Lanjutan**: 
    - RFM analysis untuk mengidentifikasi perilaku pengguna.

## Link Dashboard
Dashboard dapat diakses secara online melalui [Link Dashboard](https://sharingbikedashboard1.streamlit.app/ ).

## Kontak
Jika ada pertanyaan, silakan hubungi saya di [khamimahusriyatu@gmail.com](khamimahusriyatu@gmail.com).

