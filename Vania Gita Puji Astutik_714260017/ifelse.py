# ===================================================
# Tugas Mandiri 1 - Pemrograman Dasar
# Nama : Vania Gita Puji Astutik
# NIM : 714260017
# Kelas : 11

print("===================================")
print("    Pengolahan Nilai ")
print("===================================")

nilai = float(input("Masukkan nilai (0-100): "))

if nilai > 100:
    print("Nilai yang anda masukkan tidak valid. Silakan masukkan nilai antara 0 hingga 100.")
elif nilai >= 80:
    print(f"Nilai anda {nilai} setara dengan A")
    print("Selamat, anda lulus dengan predikat sangat baik.")
elif nilai >= 70:
    print(f"Nilai anda {nilai} setara dengan B")
    print("Selamat, anda lulus dengan predikat baik.")
elif nilai >= 60:
    print(f"Nilai anda {nilai} setara dengan C")
    print("Selamat, anda lulus dengan predikat cukup.")
elif nilai >= 50:
    print(f"Nilai anda {nilai} setara dengan D")
    print("Selamat, anda lulus dengan predikat cukup.")
elif nilai >= 0:
    print(f"Nilai anda {nilai} setara dengan E")
    print("Maaf, anda tidak lulus.")

else: 
     print("Nilai yang anda masukkan tidak valid. Silakan masukkan nilai antara 0 hingga 100.")