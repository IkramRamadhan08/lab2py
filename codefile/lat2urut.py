# Program sederhana mengurutkan 3 bilangan dari terkecil ke terbesar
print("=== Program Pengurutan 3 Bilangan ===")

# Input tiga bilangan
a = int(input("Masukkan bilangan pertama (a): "))
b = int(input("Masukkan bilangan kedua (b): "))
c = int(input("Masukkan bilangan ketiga (c): "))

# Proses pengurutan menggunakan if else
if a <= b and a <= c:
    if b <= c:
        print("Urutan dari terkecil ke terbesar:", a, b, c)
    else:
        print("Urutan dari terkecil ke terbesar:", a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print("Urutan dari terkecil ke terbesar:", b, a, c)
    else:
        print("Urutan dari terkecil ke terbesar:", b, c, a)
else:
    if a <= b:
        print("Urutan dari terkecil ke terbesar:", c, a, b)
    else:
        print("Urutan dari terkecil ke terbesar:", c, b, a)
