## Laporan Hasil Praktikum Jaringan Komputer Modul 6

# 1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara 
komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga 
teridentifikasi sebagai segmen SYN? 
![](assets/1.png)
Nomor urut (sequence number) pada segmen TCP SYN adalah 0. Segmen ini dapat dikenali sebagai SYN karena memiliki nilai flag SYN = 1 dan ACK = 0, yang menandakan awal proses pembentukan koneksi.

# -

# 2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien 
sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? 
Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen  
sehingga teridentifikasi sebagai segmen SYNACK? 
<img src="../assets/6-2-1.png">
Nomor urut (sequence number) pada segmen TCP SYN adalah 0. Identifikasi sebagai segmen SYN dilakukan berdasarkan keberadaan flag SYN = 1 dan ACK = 0, yang menunjukkan bahwa segmen tersebut digunakan untuk memulai koneksi TCP.

# -

# 3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk 
menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian 
bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATA
nya. 
<img src="../assets/6-3-1.png">
Nomor urut segmen TCP yang mengandung perintah HTTP POST adalah 1, yang merupakan kelanjutan setelah proses handshake TCP selesai.

# -

# 4. Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. 
Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi 
HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen 
diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan 
acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut? 
Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki 
fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. 
Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time 
Graph). 
<img src="../assets/6-4-1.png">
Segmen TCP yang berisi HTTP POST dianggap sebagai segmen pertama dengan sequence number awal = 1 (relative). Enam segmen pertama memiliki nomor urut yang meningkat sesuai dengan jumlah byte yang dikirim pada tiap segmen. Waktu pengiriman setiap segmen diperoleh dari kolom Time di Wireshark, sedangkan waktu diterimanya ACK ditentukan dari paket balasan dengan nilai Acknowledgement Number yang sesuai. Selisih antara waktu pengiriman segmen dan waktu penerimaan ACK menghasilkan nilai RTT untuk masing-masing segmen, yang berada pada kisaran ratusan milidetik dan menunjukkan adanya variasi kondisi jaringan. Nilai EstimatedRTT dihitung secara bertahap menggunakan metode rata-rata berbobot dari RTT sebelumnya, sehingga nilainya lebih stabil dibandingkan RTT aktual dan mengikuti tren perubahan RTT secara lebih halus.

# -

# 5. Berapa panjang setiap enam segmen TCP pertama? 
<img src="../assets/6-5-1.png">
Panjang enam segmen TCP pertama dapat dilihat pada field TCP segment length, di mana sebagian besar segmen memiliki ukuran sekitar 1460 byte, sesuai dengan ukuran maksimum payload pada jaringan Ethernet (MSS). Segmen pertama yang membawa HTTP POST umumnya berukuran lebih kecil karena memuat header tambahan, sedangkan segmen-segmen berikutnya cenderung menggunakan ukuran maksimum. Hal ini menunjukkan bahwa data besar dipecah menjadi beberapa segmen kecil agar dapat dikirim secara efisien melalui jaringan.

# -

# 6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan 
diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah 
menghambat pengiriman? 
<img src="../assets/6-6-1.png">
Nilai window size merepresentasikan kapasitas buffer yang tersedia pada sisi penerima. Berdasarkan hasil pengamatan, tidak terdapat indikasi hambatan dalam pengiriman data karena buffer penerima tidak mengalami kondisi penuh.

# -

# 7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di 
dalam file trace) untuk menjawab pertanyaan ini? 
<img src="../assets/6-7-1.png">
Tidak ditemukan adanya proses retransmission pada file trace yang dianalisis. Hal ini dibuktikan dengan tidak munculnya label “TCP Retransmission” pada paket di Wireshark, serta tidak adanya pengiriman ulang paket dengan nomor urut (sequence number) yang sama.

# -

# 8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda 
mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang 
diterima? 
<img src="../assets/6-8-1.png">
Penerima umumnya memberikan acknowledgement (ACK) terhadap sejumlah byte data secara kumulatif. Namun, pada beberapa kondisi tertentu, dapat diamati bahwa ACK dikirimkan untuk setiap segmen yang diterima.

# -

# 9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? 
Jelaskan bagaimana Anda menghitung nilai ini. 
<img src="../assets/6-9-1.png">
Throughput koneksi TCP dihitung dengan membandingkan total data yang ditransfer dengan total waktu transmisi. Total data yang dikirim terlihat dari peningkatan sequence number hingga sekitar 164090 byte, sedangkan waktu transmisi diperoleh dari selisih waktu antara awal pengiriman hingga segmen terakhir diterima. Nilai throughput diperoleh dengan membagi total byte dengan total waktu tersebut. Pola kenaikan sequence number yang stabil menunjukkan bahwa data dikirim secara kontinu tanpa retransmission, sehingga throughput yang dihasilkan mencerminkan performa jaringan yang baik dan relatif stabil.