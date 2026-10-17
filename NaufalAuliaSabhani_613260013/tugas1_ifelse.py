# ==========================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Naufal Aulia Sabhani
# NIM   : 613260013
# Kelas : D3 TI 11
# ==========================================

print("=============================================")
print("      PROGRAM KONVERSI NILAI MAHASISWA       ")
print("=============================================")

# Seluruh nilai wajib berasal dari input()
nilai_input = input("Masukkan nilai akhir (0-100): ")
nilai = float(nilai_input)

print("-" * 45)

# Pengecekan agar nilai di luar 1-100 di tolak
if nilai < 0 or nilai > 100:
    print("Error: Nilai ditolak! Harap masukkan angka dalam rentang 0-100.")

elif nilai >= 80:
    huruf_mutu = "A"
    keterangan = "Lulus"
elif nilai >= 70:
    huruf_mutu = "B"
    keterangan = "Lulus"
elif nilai >= 60:
    huruf_mutu = "C"
    keterangan = "Lulus"
elif nilai >= 50:
    huruf_mutu = "D"
    keterangan = "Tidak Lulus"
else:
    huruf_mutu = "E"
    keterangan = "Tidak Lulus"

# f-strings digunakan untuk menampilkan nilai, huruf mutu, dan keterangan
if 0 <= nilai <= 100:
    print(f"Nilai Angka  : {nilai}")
    print(f"Huruf Mutu   : {huruf_mutu}")
    print(f"Keterangan   : {keterangan}")

print("=============================================")
print("  Terima kasih telah menggunakan program ini! ")
print("=============================================")