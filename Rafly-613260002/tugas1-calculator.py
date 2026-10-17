print("===========================")
print("kalkulator konsol sederhana")
print("===========================")
print("operasi tersedia : + - * /")
print("===========================")
#bagian masukan pengguna
angka1 = float (input("masukan bilangan pertama : "))
angka2 = float (input("masukan bilangan kedua : "))
operator = input("masukan operator ( + - * /): ")
print("===========================")
#bagian proses

if operator == "+":
    hasil = angka1 + angka2 
    print(f"hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil= angka1 - angka2
    print(f"hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil: {angka1} * {angka2} + {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi dengan nol. ")

else:
    print(f"operator `{operator}` tidak dikenali.")
    print("gunakan salah satu dari: + - * /")
print("===========================")
print("ngajedog di imah.")
