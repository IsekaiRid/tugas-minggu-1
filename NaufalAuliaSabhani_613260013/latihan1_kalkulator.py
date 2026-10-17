def main():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ").strip()
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input tidak valid: masukkan angka.")
        return

    if operator == "+":
        hasil = angka1 + angka2
        print(f"hasil: {angka1} + {angka2} = {hasil:.2f}")
    elif operator == "-":
        hasil = angka1 - angka2
        print(f"hasil: {angka1} - {angka2} = {hasil:.2f}")
    elif operator == "*":
        hasil = angka1 * angka2
        print(f"hasil: {angka1} x {angka2} = {hasil:.2f}")
    elif operator == "/":
        if angka2 == 0:
            print("Error: Tidak bisa membagi dengan nol!")
        else:
            hasil = angka1 / angka2
            print(f"hasil: {angka1} / {angka2} = {hasil:.2f}")
    else:
        print("Operator input tidak valid! Silakan pilih +, -, *, atau /")

print ("=== KALKULATOR SEDERHANA ===")

if __name__ == "__main__":
    main()

print ("=== Terima kasih telah menggunakan kalkulator sederhana ===")