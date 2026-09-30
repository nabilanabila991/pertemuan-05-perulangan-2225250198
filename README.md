# Pertemuan 05 Perulangan Python

Nama: Mafatihun Nabila
NIM: 2225250198
Kelas: 3B

## Tujuan

Menggunakan perulangan `for` dan `while` untuk menyelesaikan masalah iteratif, seperti membuat tabel perkalian, menghitung jumlah bilangan, melakukan validasi input, menghitung bilangan genap, dan membuat deret aritmetika.

## Cara Menjalankan

Untuk menjalankan program Kuis 2, gunakan perintah berikut pada terminal:

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

Pada Windows, jika `python3` tidak dapat digunakan, dapat menggunakan:

```bash
python kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

1. Menampilkan judul program **Deret Aritmetika**.
2. Membaca suku pertama `a` sebagai bilangan desimal.
3. Membaca beda `d` sebagai bilangan desimal.
4. Membaca banyak suku `n` sebagai bilangan bulat.
5. Memeriksa nilai `n` menggunakan `while`.
6. Jika `n` kurang dari atau sama dengan 0, program meminta pengguna memasukkan `n` kembali.
7. Jika `n` sudah positif, variabel `total` diatur menjadi 0.
8. Menggunakan `for` untuk mengulang sebanyak `n` kali.
9. Pada setiap perulangan, menghitung nilai suku berdasarkan suku pertama, beda, dan nomor perulangan.
10. Menambahkan nilai suku ke dalam `total`.
11. Menampilkan nomor dan nilai setiap suku.
12. Setelah perulangan selesai, menampilkan jumlah seluruh suku dengan dua angka di belakang koma.

## Hasil Pengujian

| No. | Input (a, d, n) | Keluaran yang Diharapkan        | Keluaran Aktual                 | Status   |
| --- | --------------- | ------------------------------- | ------------------------------- | -------- |
| 1   | 2, 3, 5         | 2, 5, 8, 11, 14; Jumlah = 40.00 | 2, 5, 8, 11, 14; Jumlah = 40.00 | Berhasil |
| 2   | 10, -2, 4       | 10, 8, 6, 4; Jumlah = 28.00     | 10, 8, 6, 4; Jumlah = 28.00     | Berhasil |
| 3   | 1.5, 0.5, 3     | 1.5, 2.0, 2.5; Jumlah = 6.00    | 1.5, 2.0, 2.5; Jumlah = 6.00    | Berhasil |

### Pengujian Validasi

Ketika `n` diberi nilai `0` atau bilangan negatif, program menampilkan pesan bahwa banyak suku harus positif dan meminta input kembali sampai mendapatkan nilai `n` yang valid.

## Refleksi

Kesalahan yang ditemukan adalah kesalahan pada batas perulangan, yaitu menggunakan `range(n - 1)` sehingga jumlah suku yang ditampilkan kurang satu. Kesalahan tersebut diperbaiki dengan menggunakan `range(n)`, sehingga perulangan berjalan tepat sebanyak `n` kali. Selain itu, variabel `total` harus diinisialisasi sebelum perulangan agar setiap suku dapat ditambahkan secara bertahap.