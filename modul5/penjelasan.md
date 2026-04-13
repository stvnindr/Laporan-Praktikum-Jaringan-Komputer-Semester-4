# Laporan Hasil Praktikum Jaringan Komputer Modul 5

## Tampilan Wireshark UDP
![](assets/1.png)

1. Komposisi Field Header UDP
Berdasarkan hasil tangkapan paket (capture), header UDP memiliki struktur yang sederhana dengan 4 komponen utama, yakni:
- Source Port: Port asal pengirim.
- Destination Port: Port tujuan penerima.
- Length: Ukuran total segmen.
- Checksum: Digunakan untuk verifikasi integritas data.

---

2. Dimensi Ukuran Field

Masing-masing dari keempat field di atas memiliki ukuran tetap sebesar 16 bit (2 byte). Dengan demikian, total akumulasi ukuran header UDP tanpa data tambahan adalah 8 byte.

---

3. Interpretasi Nilai "Length"

Indikator Length pada header mencerminkan ukuran keseluruhan dari paket UDP tersebut. Nilai ini didapatkan dari hasil penjumlahan antara panjang header (8 byte) dengan ukuran payload (data) yang dibawa.

---

4. Kapasitas Maksimum Payload

Mengingat field panjang (Length) dibatasi oleh alokasi 16 bit, nilai total maksimum yang bisa ditampung adalah $2^{16} - 1 = 65.535$ byte. Setelah dikurangi oleh ukuran header UDP sebesar 8 byte, maka kapasitas bersih maksimal untuk data (payload) adalah 65.527 byte.

---

5. Batas atas nomor port

Rentang nomor port UDP ditentukan oleh panjang 2 byte, sehingga nilai tertinggi yang dapat dialokasikan untuk sebuah layanan atau aplikasi adalah 65.535.

---

6. Identitas Protokol UDP

Dalam tumpukan protokol internet (IP Header), UDP diidentifikasi secara unik dengan nomor protokol:
- Format Desimal: 17
- Format Heksadesimal: 0x11

---

7. Mekanisme Port pada Request dan Response

Terdapat pola simetris dalam pertukaran paket UDP. Saat sebuah paket balasan (response) dikirimkan, posisi port akan mengalami pembalikan: port asal pada paket permintaan (request) akan berperan sebagai port tujuan pada paket balasan, dan sebaliknya.