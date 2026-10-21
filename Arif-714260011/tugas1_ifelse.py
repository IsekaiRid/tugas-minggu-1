# ==========================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Arif Hidayatulloh
# NIM   : 714260011 
# Kelas : D4 TI 11
# ==========================================

print("=============================================")
print("      PROGRAM KONVERSI NILAI MAHASISWA       ")
print("=============================================")

nilai_input = input("Masukkan nilai akhir (0-100): ")
nilai = float(nilai_input)

print("-" * 45)

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

if 0 <= nilai <= 100:
    print(f"Nilai Angka  : {nilai}")
    print(f"Huruf Mutu   : {huruf_mutu}")
    print(f"Keterangan   : {keterangan}")

print("=============================================")
print("  Terima kasih telah menggunakan program ini! ")
print("=============================================")