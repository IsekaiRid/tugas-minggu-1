# =================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : RIDHWAN SULAIMAN SUZANA
# NIM   : 714260026
# Kelas : D4-TI 1B
# Kelompok : 5 BURGERKILL
# =================================================
 
print("========================================")
print("    MELIHAT HURUF MUTU NILAI")
print("========================================")

nilai = int(input("MASUKAN NILAI AKHIR (0-100):"))

print("----------------------------------------")
if nilai < 0 or nilai > 100:
    print("KESALAHAN: NILAI HARUS BERADA DI RENTANG 0-100")
elif nilai >= 80:
    print(F"NILAI KAMU {nilai} -> HURUF MUTU: A (SANGAT BAIK)")
elif nilai >= 70:
    print(F"NILAI KAMU {nilai} -> HURUF MUTU: B (BAIK)")
elif nilai >= 55:
    print(F"NILAI KAMU {nilai} -> HURUF MUTU: C (CUKUP)")
elif nilai >= 40:
    print(F"NILAI KAMU {nilai} -> HURUF MUTU: D (KURANG)")
else:
    print(F"NILAI KAMU {nilai} -> HURUF MUTU: E (SANGAT KURANG)")

print("----------------------------------------")
print("=============TERIMA=KASIH===============")