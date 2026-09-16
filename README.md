# Pertemuan 03 Seleksi Python

**Nama:** [Sela Widiyanti]
**NIM:** [2225250176]
**Kelas:** [3F]

## Tujuan

Pada pertemuan ini, saya mempelajari penggunaan seleksi dalam Python, yaitu `if`, `if-else`, kondisi majemuk, dan `nested if`.

Program yang dibuat meliputi:

* Menentukan bilangan genap atau ganjil.
* Membandingkan dua bilangan.
* Menentukan kelulusan berdasarkan nilai dan kehadiran.
* Menentukan jenis segitiga.
* Menganalisis persamaan kuadrat berdasarkan nilai diskriminan.

## Struktur Folder

```text
pertemuan-03-seleksi-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_genap_ganjil.py
│   ├── 02_bandingkan_dua_bilangan.py
│   ├── 03_kelulusan_bersyarat.py
│   └── 04_jenis_segitiga.py
└── tugas/
    └── analisis_persamaan_kuadrat.py
```

## Cara Menjalankan

Program dijalankan menggunakan Python melalui terminal VS Code.

Contoh untuk menjalankan tugas analisis persamaan kuadrat:

```bash
python tugas/analisis_persamaan_kuadrat.py
```

Untuk menjalankan latihan, gunakan perintah:

```bash
python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
```

## Algoritma Tugas

### Analisis Persamaan Kuadrat

1. Memasukkan nilai koefisien `a`, `b`, dan `c`.
2. Memeriksa apakah nilai `a` sama dengan 0.
3. Jika `a = 0`, maka program menampilkan bahwa persamaan bukan persamaan kuadrat.
4. Jika `a ≠ 0`, menghitung diskriminan dengan rumus:

```text
D = b² - 4ac
```

5. Jika `D > 0`, persamaan mempunyai dua akar real yang berbeda.
6. Jika `D = 0`, persamaan mempunyai satu akar real kembar.
7. Jika `D < 0`, persamaan tidak mempunyai akar real.

## Hasil Pengujian

### 1. Bilangan Genap/Ganjil

| Input | Keluaran yang Diharapkan | Status   |
| ----- | ------------------------ | -------- |
| 8     | Genap                    | Berhasil |
| 13    | Ganjil                   | Berhasil |
| 0     | Genap                    | Berhasil |
| -7    | Ganjil                   | Berhasil |

### 2. Membandingkan Dua Bilangan

| Input (a, b) | Keluaran yang Diharapkan | Status   |
| ------------ | ------------------------ | -------- |
| 7, 4         | a lebih besar dari b     | Berhasil |
| 2, 9         | a lebih kecil dari b     | Berhasil |
| 5, 5         | a sama dengan b          | Berhasil |
| -3, -8       | a lebih besar dari b     | Berhasil |

### 3. Kelulusan Bersyarat

Syarat kelulusan adalah nilai minimal **60** dan kehadiran minimal **80%**.

| Nilai | Kehadiran | Keluaran yang Diharapkan | Status   |
| ----: | --------: | ------------------------ | -------- |
|    75 |        90 | Lulus                    | Berhasil |
|    59 |        90 | Tidak lulus              | Berhasil |
|    75 |        79 | Tidak lulus              | Berhasil |
|    60 |        80 | Lulus                    | Berhasil |

### 4. Jenis Segitiga

| Sisi (a, b, c) | Keluaran yang Diharapkan | Status   |
| -------------- | ------------------------ | -------- |
| 3, 3, 3        | Segitiga sama sisi       | Berhasil |
| 5, 5, 8        | Segitiga sama kaki       | Berhasil |
| 3, 4, 5        | Segitiga sembarang       | Berhasil |
| 1, 2, 3        | Bukan segitiga           | Berhasil |

### 5. Analisis Persamaan Kuadrat

| Input (a, b, c) | Diskriminan | Keluaran yang Diharapkan            | Status   |
| --------------- | ----------: | ----------------------------------- | -------- |
| 1, -5, 6        |           1 | Dua akar real: x1 = 3.00, x2 = 2.00 | Berhasil |
| 1, 2, 1         |           0 | Akar real kembar: x = -1.00         | Berhasil |
| 1, 0, 1         |          -4 | Tidak ada akar real                 | Berhasil |
| 0, 2, 3         |           - | Bukan persamaan kuadrat             | Berhasil |

## Refleksi

Pada latihan ini saya mempelajari cara menggunakan percabangan dalam Python untuk membuat keputusan berdasarkan kondisi tertentu.

Salah satu hal yang perlu diperhatikan adalah penggunaan operator perbandingan dan operator logika. Kesalahan pada kondisi dapat menyebabkan keluaran program tidak sesuai dengan yang diharapkan.

Melalui pengujian dengan beberapa kondisi, termasuk nilai batas seperti `0`, `60`, dan `80`, saya dapat memastikan bahwa logika program berjalan sesuai dengan aturan yang diberikan.

## Kesimpulan

Pada pertemuan ini saya telah mempraktikkan penggunaan `if`, `if-else`, kondisi majemuk, dan `nested if` dalam Python. Saya juga melakukan pengujian terhadap beberapa kondisi untuk memastikan program menghasilkan keluaran yang sesuai.
