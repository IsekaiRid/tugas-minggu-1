print("========================================")
print("     KALKULATOR KONSOL SEDERHANA")
print("========================================")
print("Operasi tersedia: +  -  *  /")
print("----------------------------------------")

angka1 = int(input("MASUKAN ANGKA:"))
angka2 = int(input("MASUKAN ANGKA:"))
operator = input("PILIH PERHITUNGAN OPERATOR ( + , - , * , / ) :")

print("----------------------------------------")
if operator == "+":
    hasil = angka1 + angka2
    print(F"HASIL PERJUMLAHAN {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(F"HASIL PENGURANGAN {angka1} - {angka2} = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(F"HASIL PERKALIAN {angka1} * {angka2} = {hasil}")
elif operator == "/":
    if angka2 == 0 or angka1 == 0:
        print("KESALAHAN: BILANGAN TIDAK BISA DI BAGI NOL")
    else:
        hasil = angka1 / angka2
        print(F"HASIL :{angka1} / {angka2} = {hasil}")
       
else:
    print(F"OPERATOR '{operator}' TIDAK DI KENALI!")
    print("Gunakan operasi yang tersedia: +  -  *  /")

print("========================================")
print("Terima Kasih Telah Menggunakan Kakulator Ini")