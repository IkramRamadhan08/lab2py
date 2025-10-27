# Program Menentukan Bilangan Terbesar dari 4 Bilangan
print("=== Program Menentukan Bilangan Terbesar ===")

# Input empat bilangan
a = int(input("Masukkan bilangan pertama (a): "))
b = int(input("Masukkan bilangan kedua (b): "))
c = int(input("Masukkan bilangan ketiga (c): "))
d = int(input("Masukkan bilangan keempat (d): "))

# Menentukan bilangan terbesar menggunakan if bertingkat
if a > b:
    if a > c:
        if a > d:
            terbesar = a
        else:
            terbesar = d
    else:
        if c > d:
            terbesar = c
        else:
            terbesar = d
else:
    if b > c:
        if b > d:
            terbesar = b
        else:
            terbesar = d
    else:
        if c > d:
            terbesar = c
        else:
            terbesar = d

# Output hasil
print(f"Bilangan terbesar dari ({a}, {b}, {c}, {d}) adalah: {terbesar}")
