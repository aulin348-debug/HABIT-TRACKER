import pandas as pd
import streamlit as st

st.set_page_config(page_title="Biodata Habit Tracker", layout="wide")
st.title("Aplikasi Biodata & Habit Tracker (50 Entri)")

# 1. Membuat 50 data dummy biodata & tracker
data = []
for i in range(1, 51):
    data.append(
        {
            "No": i,
            "Nama": f"Pengguna {i}",
            "Kebiasaan Target": "Membaca 15 Menit",
            "Senin": False,
            "Selasa": False,
            "Rabu": False,
            "Kamis": False,
            "Jumat": False,
            "Sabtu": False,
            "Minggu": False,
        }
    )

df = pd.DataFrame(data)

# 2. Menampilkan tabel interaktif yang bisa dicentang
st.write("Silakan centang kebiasaan yang berhasil diselesaikan:")
edited_df = st.data_editor(df, num_rows="dynamic")

# 3. Menghitung total centang
edited_df["Total Selesai"] = edited_df[
    ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
].sum(axis=1)

# 4. Menampilkan hasil ringkasan
st.subheader("Ringkasan Kemajuan")
st.dataframe(edited_df[["No", "Nama", "Kebiasaan Target", "Total Selesai"]])