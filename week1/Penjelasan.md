# Cara Penggunaan WireShark: Interupting & Analysing Traffic Network

Pada file ini saya akan menjelaskan langkah-langkah dasar melakukan pemantauan traffic network menggunakan Wireshark untuk analisis keamanan web melalui jaringan.

---

## 1. Persiapan Tools

Langkah awal adalah membuka aplikasi Wireshark.

![Gambar 1](Assets/01.png)
* **Langkah:** Open **lalu akan muncul tampilan seperti gambar dibawah ini**.

![Gambar 2](Assets/1.png)
* **Langkah:** Pilih **Wifi** lalu Klik **Enter**.

---

## 2. Analisis Trafic Network (lalu lintas jaringan)

Dibawah ini adalah lalu lintas jaringan pada wifi yang sedang saya gunakan sekarang ini.

![Gambar 3](Assets/2.png)

---

## 3. konfigurasi Proses Capture

Proses mengatur konfigurasi proses capture (penangkapan paket data) sebelum Wireshark mulai merekam traffic jaringan.

![Gambar 4](Assets/3.png)
* **Langkah:** Klik Capture lalu **Option**. Lalu akan muncul tampilan seperti gambar dibawah ini.

![Gambar 5](Assets/4.png)
* **Langkah:** Pilih interface mana yang ingin anda lakukan penangkapan paket nya, Disini saya akan melakukan pada **wifi** Pilih **Wi-Fi** lalu klik **Start**.

![Gambar](Assets/5.png)
* **Langkah:** Jika muncul seperti itu klik saja yang tengah **Continue without Saving**. Lalu akan muncul tampilan seperti gambar dibawah ini.

![Gambar](Assets/10.png)
Jika sudah maka akan muncul semua aktivitas lalulintas dari wifi yang digunakan.

---

## 4. Analisis HTTP History

Melihat rekam jejak semua request yang telah melalui proxy.

![Gambar 6](Assets/6.png)
* **Langkah:** Buka browser apa saja lalu ketikkan link pada gambar tersebut **HTTP jangan HTTPS ya**.

![Gambar 7](Assets/11.png)
* **Maka akan muncul tampilan web seperti itu**.

![Gambar 7](Assets/7.png)
* **Langkah:** Kembali ke **wireshark** lalu pada bagian filter ketikkan **http** sampai background berwarna hijau dan klik **enter**.

![Gambar 8](Assets/8.png)
* **Detail:** Klik pada salah satu baris history yang berwarna ungu pada gambar tersebut untuk melihat detail **Request** (data yang dikirim) dan **Response** (balasan dari server) di panel bagian bawah.

![Gambar 9](Assets/9.png)
* **Detail:** Bisa kita lihat pesan yang ada di web sebelumnya terlihat di history paket juga.

---
