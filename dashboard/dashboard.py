import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Dashboard Penggunaan Sepeda",
    layout="wide"
)

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


# Pastikan data sudah dimuat dengan benar sebelum mengaksesnya
if not hour_df.empty and not day_df.empty:
    st.title("Dashboard Penggunaan Sepeda🚲")
    st.markdown("<p style='text-align: center;'></p>", unsafe_allow_html=True)


    
 # Scoreboard
    total_rides = hour_df['cnt'].sum()
    avg_temp = hour_df['temp'].mean()
    total_days = day_df['dteday'].nunique()
    # Layout untuk scoreboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Penggunaan Sepeda", f"{total_rides:,}")
    
    with col2:
        st.metric("Rata-Rata Suhu (°C)", f"{avg_temp:.2f}")
    
    with col3:
        st.metric("Total Hari dalam Dataset", f"{total_days}")

    # Pilihan untuk pengguna
    st.sidebar.header("Opsi Filter")
    selected_day = st.sidebar.selectbox("Pilih Hari dalam Seminggu", 
                                        options=hour_df['weekday'].unique(),
                                        format_func=lambda x: ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"][x])

    # Menggunakan dictionary untuk pemetaan musim
    season_mapping = {0: "Musim Semi", 1: "Musim Panas", 2: "Musim Gugur", 3: "Musim Dingin"}
    valid_seasons = [season for season in day_df['season'].unique() if season in season_mapping]

    selected_season = st.sidebar.selectbox("Pilih Musim", 
                                           options=valid_seasons,
                                           format_func=lambda x: season_mapping.get(x, "Musim Tidak Dikenal"))

 # Konfigurasi Plot
    def plot_weather_impact():
        st.subheader("Pengaruh Cuaca terhadap Penggunaan Sepeda")
        st.write("Visualisasi ini menunjukkan bagaimana kondisi cuaca mempengaruhi jumlah penggunaan sepeda.")
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=hour_df, x='temp', y='cnt', hue='weathersit', palette='coolwarm', alpha=0.6)
        plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda', fontsize=16)
        plt.xlabel('Suhu (temp)', fontsize=14)
        plt.ylabel('Jumlah Penggunaan Sepeda (cnt)', fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        st.pyplot(plt)
        plt.close()  # Tutup plot untuk mencegah tumpang tindih

    def plot_usage_trends():
        st.subheader("Tren Penggunaan Sepeda Berdasarkan Waktu")
        st.write("Tren penggunaan sepeda ini ditampilkan berdasarkan waktu dalam sehari dan musim dalam setahun.")
        
        # Plot per jam berdasarkan hari dalam seminggu
        plt.figure(figsize=(10, 6))
        filtered_hour_df = hour_df[hour_df['weekday'] == selected_day]
        sns.lineplot(data=filtered_hour_df, x='hr', y='cnt', hue='weekday', palette='viridis')
        plt.title(f'Tren Penggunaan Sepeda pada {["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"][selected_day]}', fontsize=16)
        plt.xlabel('Jam', fontsize=14)
        plt.ylabel('Jumlah Penggunaan Sepeda (cnt)', fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        st.pyplot(plt)
        plt.close()  # Tutup plot untuk mencegah tumpang tindih
       # Plot per hari berdasarkan musim
        st.subheader("Tren Penggunaan Sepeda Berdasarkan Musim")
        st.write("Grafik ini menunjukkan tren penggunaan sepeda sepanjang tahun berdasarkan musim yang dipilih.")
        
        # Pastikan kolom 'dteday' diformat sebagai datetime
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        
        plt.figure(figsize=(12, 6))
        filtered_day_df = day_df[day_df['season'] == selected_season]
        sns.lineplot(data=filtered_day_df, x='dteday', y='cnt', hue='season', palette='magma')
        plt.title(f'Tren Penggunaan Sepeda pada {season_mapping[selected_season]}', fontsize=16)
        plt.xlabel('Tanggal', fontsize=14)
        plt.ylabel('Jumlah Penggunaan Sepeda (cnt)', fontsize=14)
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        st.pyplot(plt)
        plt.close()  # Tutup plot untuk mencegah tumpang tindih

# Menampilkan plot di Streamlit
plot_weather_impact()
plot_usage_trends()

# Tambahan Footer
st.markdown("""
    ---  
    **Dashboard Penggunaan Sepeda**  
    Dibuat oleh: Usriyatul Khamimah
""")
