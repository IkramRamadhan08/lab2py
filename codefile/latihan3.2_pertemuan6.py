print("=== Program Kalkulator Sederhana ===")

# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

# Proses perhitungan
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Tidak bisa dibagi dengan nol!"
else:
    hasil = "Operator tidak dikenal!"

# Output hasil
print("\n=== Hasil Perhitungan ===")
print(f"{angka1} {operator} {angka2} = {hasil}")
