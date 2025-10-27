# Pertemuan 6
## Tugas Pengantar Pemograman 
Ini adalah pertemuan 3 dari ikram ramadhan dengan dosen pengampu bapak Agung Nugroho, S.Kom., M.Kom

````shell
Nama   : Ikram Ramadhan
Nim    : 312110478
Matkul : Pengantar Pemograman
````
## code bertahap menggunakan screenshoot
````shell

nama = input("Masukkan nama: ")
uts = input("Masukkan nilai UTS: ")
uas = input("Masukkan nilai UAS: ")
tugas = input("Masukkan nilai Tugas: ")

akhir = (int(tugas) * 0.2) + (int(uts) * 0.4) + (int(uas) * 0.4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nNama :", nama)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Tugas :", tugas)
print("Nilai Akhir :", akhir)
print("\nNilai Huruf :", huruf)
print("Keterangan :", keterangan)
````
* *Hasil output program:*
  ![img 1](asset/lat1code.png)
* *

## Praktek untuk mengenal variabel,masih menggunakan CMD
````shell
Variabel dalam bahasa Python adalah wadah yang digunakan untuk menyimpan nilai atau data sementara dalam memori komputer. 
stepnya;
1. ketikan variabel contoh menggunakan a sebagai variabel maka tulis a = <nilai contoh 10>, b = <nilai contoh 13>.
2. beri perintah print contoh print("variabel a=",a) a diluar tutup petik dua setelah koma adalah variabel yang telah
menyimpan nilai
3. lakukan hal yang sama untuk b
````
* *Hasil output program:*
  ![img 1](asset/variabel.png)
  * *

## Mengenal IDLE python
````shell
IDLE (Integrated Development and Learning Environment) adalah teks editor dan lingkungan pengembangan sederhana bawaan Python yang memudahkan penulisan, pengujian, dan menjalankan kode Python. 
jika anda telah mendownload python biasanya otomatis sekaligus dengan IDLE 
1. cari pada tab cari aplikasi di laptop anda.
````
* *Hasil output progragim:*
  ![img 1](asset/idle.png)
  * *

````shell
2. ketik kode pengenalan operasi dasar python seperti di contoh screenshoot
````
* *Hasil output progragim:*
  ![img 1](asset/idle.png)
  * *
````shell
3. maka kita akan mendapatkan hasil seperti berikut
````
* *Hasil output progragim:*
  ![img 1](asset/hasil.png)
  * *