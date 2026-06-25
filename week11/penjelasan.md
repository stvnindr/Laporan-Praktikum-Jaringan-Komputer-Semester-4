# Modul 11 DHCP (*Dynamic Host Configuration Protocol*)
### Mekanisme Pengalamatan Dinamis menggunakan Wireshark

Nama    : Steven Indramer
NIM     : 103072400070
Kelas   : IF-04-04

---


## 📖 Teori 
Dalam protokol DHCP, ada 4 tahap untuk memberikan alamat IP kepada klien, yaitu
1. **DHCP Discover**. Klien menyiarkan pesan untuk mencari server DHCP yang tersedia.
2. **DHCP Offer**. Server merespons dengan tawaran alamat IP dan parameter konfigurasi lainnya.
3. **DHCP Request**. Klien meminta alamat IP yang ditawarkan tersebut kepada server.
4. **DHCP ACK**. Server memberikan konfirmasi akhir bahwa alamat IP telah resmi dipinjamkan (*lease*).

---

## 🚀 Langkah Praktikum
1. Jalankan Wireshark dan pilih jaringan yang aktif.
2. Gunakan filter `dhcp` atau `bootp` pada Wireshark.
3. Buka Terminal/CMD sebagai Administrator.
4. Jalankan perintah `ipconfig /release` untuk melepaskan IP saat ini.

![ipconfig /release](../week11/Assets/1.png)

5. Mulai tangkap paket-paket yang akan muncul di Wireshark.
6. Jalankan perintah `ipconfig /renew` untuk meminta IP baru dari server.

![ipconfig /renew](../week11/Assets/2.png)

7. Setelah beberapa detik, *stop capture* di Wireshark.

![hasil capture](../week11/Assets/3.png)

---

## Analisis Paket DHCP

Berdasarkan hasil tangkapan paket (*trace*), berikut adalah poin-poin analisis utama:

### 1. Transport Layer (UDP)
DHCP beroperasi menggunakan protokol **UDP**.
* **Source Port**: 68.
* **Destination Port**: 67.

### 2. Identifikasi Pesan DORA
| Tipe Pesan | Source IP | Destination IP | Deskripsi |
| :--- | :--- | :--- | :--- |
| **Discover** | `0.0.0.0` | `255.255.255.255` | Broadcast mencari server. |
| **Offer** | `10.218.0.253` | `10.218.2.21` | Tawaran IP dari server. |
| **Request** | `0.0.0.0` | `255.255.255.255` | Permintaan dari klien. |
| **ACK** | `10.218.0.253` | `10.218.2.21` | Konfirmasi dari server. |

### 3. Field Penting dalam Header DHCP
* **Transaction ID**. Angka unik (contoh: `0xbc42c45e`) yang digunakan untuk mencocokkan permintaan klien dengan balasan server.
* **Client IP Address**. Alamat IP yang ditawarkan oleh server kepada klien.


## Kesimpulan
Melalui praktikum ini, mekanisme *connectionless* dari DHCP terlihat jelas melalui penggunaan UDP dan alamat broadcast (`255.255.255.255`) karena pada tahap awal klien belum memiliki identitas IP. Penggunaan **Transaction ID** sangat krusial untuk memastikan klien menerima konfigurasi yang tepat di tengah lalu lintas jaringan yang padat.


