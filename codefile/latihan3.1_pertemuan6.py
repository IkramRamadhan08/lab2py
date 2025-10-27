print("=== Program Hitung Harga Tiket Bioskop ===")

# Input tipe tiket
tipe = input("Pilih tipe tiket (Reguler/VIP): ").lower()
member = input("Apakah Anda memiliki kartu member? (Y/T): ").upper()

# Tentukan harga berdasarkan tipe tiket
if tipe == "reguler":
    harga = 50000
elif tipe == "vip":
    harga = 100000
else:
    print("Tipe tiket tidak valid!")
    exit()  # keluar dari program jika input salah

# Cek apakah user memiliki kartu member
if member == "Y":
    diskon = 0.2 * harga
else:
    diskon = 0

# Hitung total harga setelah diskon
total = harga - diskon

# Tampilkan hasil
print("\n=== Rincian Pembayaran ===")
print(f"Tipe Tiket     : {tipe.capitalize()}")
print(f"Harga Tiket    : Rp{harga:,}")
print(f"Diskon         : Rp{int(diskon):,}")
print(f"Total Bayar    : Rp{int(total):,}")
