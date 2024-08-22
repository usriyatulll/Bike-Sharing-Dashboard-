import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Dashboard Sepeda",
    layout="wide"
)

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    try:
        hour_df = pd.read_csv('data/hour.csv')  # Ganti dengan path yang sesuai
        day_df = pd.read_csv('data/day.csv')    # Ganti dengan path yang sesuai
        return hour_df, day_df
    except FileNotFoundError as e:
        st.error(f"File tidak ditemukan: {e.filename}")
        return None, None

# Memuat data
hour_df, day_df = load_data()
if hour_df is None or day_df is None:
    st.stop()  # Hentikan eksekusi jika file tidak ditemukan

# Konfigurasi Plot
def plot_weather_impact():
    st.subheader("Pengaruh Cuaca terhadap Penggunaan Sepeda")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=hour_df, x='temp', y='cnt', hue='weathersit', palette='viridis', alpha=0.6)
    plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda')
    plt.xlabel('Suhu (temp)')
    plt.ylabel('Jumlah Penggunaan Sepeda (cnt)')
    st.pyplot(plt)
    plt.close()  # Tutup plot untuk mencegah tumpang tindih

def plot_usage_trends():
    st.subheader("Tren Penggunaan Sepeda Berdasarkan Waktu")
    
    # Plot per jam
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=hour_df, x='hr', y='cnt', hue='weekday', palette='viridis')
    plt.title('Tren Penggunaan Sepeda per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Penggunaan Sepeda (cnt)')
    st.pyplot(plt)
    plt.close()  # Tutup plot untuk mencegah tumpang tindih
    
    # Plot per hari
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=day_df, x='dteday', y='cnt', hue='season', palette='viridis')
    plt.title('Tren Penggunaan Sepeda per Hari')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Penggunaan Sepeda (cnt)')
    st.pyplot(plt)
    plt.close()  # Tutup plot untuk mencegah tumpang tindih

# Menampilkan plot di Streamlit
plot_weather_impact()
plot_usage_trends()
