import random  # untuk menghasilkan bilangan acak

print("=== Program Bilangan Acak < 0.5 ===")

# Input jumlah bilangan acak
n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

count = 0  # penghitung jumlah bilangan yang sudah ditampilkan

while count < n:
    # setiap iterasi while, kita bisa buat for untuk mencoba beberapa angka
    for i in range(1):
        bilangan = random.random()  # menghasilkan angka acak 0.0–1.0
        if bilangan < 0.5:
            print(f"Bilangan ke-{count+1}: {bilangan:.4f}")
            count += 1  # tambahkan hitungan jika < 0.5
