import streamlit as st
from datetime import datetime

# Judul aplikasi
st.title("Penghitung Usia")

# Input tanggal lahir
tanggal_lahir = st.date_input("Masukkan Tanggal Lahir Anda:")

# Tombol untuk menghitung usia
if st.button("Hitung Usia"):
    # Menghitung usia
    hari_ini = datetime.now().date()
    umur = hari_ini.year - tanggal_lahir.year
    
    # Mengurangi 1 jika belum ulang tahun tahun ini
    if (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day):
        umur -= 1
    
    # Menampilkan hasil
    st.write(f"Usia Anda adalah {umur} tahun.")
