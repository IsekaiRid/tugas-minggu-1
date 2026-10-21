print("========================================")
print("        MELIHAT HURUF MUTU NILAI")
print("========================================")

nilai_input = input("MASUKAN NILAI AKHIR (0-100): ")

print("----------------------------------------")
if not nilai_input.replace('.', '', 1).isdigit():
    print("KESALAHAN: JANGAN MASUKAN HURUF ATAU STRING!")
else:
    nilai = float(nilai_input)
    mutu = None
    status = None

    if nilai < 0 or nilai > 100:
        print("KESALAHAN: NILAI HARUS BERADA DI RENTANG 0-100")
    elif nilai >= 80:
        mutu = "A"
        status = "LULUS"
    elif nilai >= 70:
        mutu = "B"
        status = "LULUS"
    elif nilai >= 55:
        mutu = "C"
        status = "LULUS"
    elif nilai >= 40:
        mutu = "D"
        status = "TIDAK LULUS"
    else:
        mutu = "E"
        status = "TIDAK LULUS"

    if 0 <= nilai <= 100:
        print(f"NILAI KAMU          : {nilai}")
        print(f"HURUF MUTU          : {mutu}")
        print(f"STATUS KAMU         : {status}")

print("----------------------------------------")
print("=============TERIMA=KASIH===============")