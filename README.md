# Webhook

- [Deskripsi](#deskripsi)
- [Fitur](#fitur)
- [Prasyarat](#prasyarat)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan-)
- [Konfigurasi Webhook di Trakteer](#konfigurasi-webhook-di-trakteer)
- [Menguji Webhook](#menguji-webhook)

## Deskripsi
Webhook ini menghubungkan platform **Trakteer** dengan **Twitter**. Server ini dirancang untuk mengambil pesan dukungan dari Trakteer dan mengirimkannya sebagai status tweet di akun Twitter yang ditentukan.

## Fitur
- Mengambil pesan dukungan dari Trakteer melalui webhook.
- Mengirim pesan tersebut ke Twitter sebagai tweet.
- Menangani kesalahan dan memberikan umpan balik yang sesuai.

## Prasyarat
Sebelum memulai, pastikan Anda memiliki hal-hal berikut:
- Python 3.12 yang sudah terinstal.
- Akun Twitter dan akses API (API Key, API Secret Key, Access Token, dan Access Token Secret).
- Akun Trakteer

## Instalasi
1. **Clone Repository**
   ```bash
   git clone https://github.com/husniadamramadhan/webhook.git
   cd webhook
2. **Buat Virtual Environment**
    ```bash
    python -m venv venv
3. **Aktifkan virtual environment**
   - di windows
       ```bash
     venv\Scripts\activate
   - di macOS
       ```bash
     source venv/bin/activate
4. **Install Dependensi**
    ```bash
   pip install -r requirements.txt
5. **Konfigurasi**
- Buat file ```.env``` di direktori root proyek dan tambahkan kredensial Anda:
   ```bash
   TWITTER_API_KEY=<your_api_key>
   TWITTER_API_KEY_SECRET=<your_api_secret_key>
   ACCESS_TOKEN=<your_access_token>
   ACCESS_TOKEN_SECRET=<your_access_token_secret>
   BEARER_TOKEN=<your_bearer_token>
   WEBHOOK_TOKEN=<your_webhook_token>
  
Catatan: Pastikan permission di [Twitter Developer Portal](https://developer.x.com/en/portal/projects-and-apps) diatur dengan benar Read and Write
Untuk webhook_token didapatkan di trakteer.

## Penggunaan 
1. **Jalankan Server**
    ```bash
   python flask_server.py
2. **Gunakan ngrok untuk mengakses server secara online**  
    Install ngrok, kemudian  jalankan ngrok dan tulis perintah di terminal:
    ```bash
   ngrok http 5000

Catat URL ngrok yang dihasilkan (misalnya https://xxxxxx.ngrok.io). URL ini akan digunakan untuk mengonfigurasi webhook di Trakteer.

## Konfigurasi Webhook di Trakteer
1. **Masuk ke Trakteer menggunakan akun Anda.**
2. **Temukan bagian konfigurasi webhook dan masukkan URL ngrok yang telah dicatat sebelumnya. Masukkan juga routenya seperti contoh https://xxxxxx.ngrok.io/webhook**.
3. **Aktifkan fitur webhook.**

## Menguji Webhook
1. **Setelah mengonfigurasi URL webhook, lakukan pengujian dengan mengirimkan data ke webhook dari Trakteer. Biasanya, terdapat tombol "Test" di halaman konfigurasi webhook.**
2. **Periksa output di terminal tempat server Flask Anda berjalan. Anda harus melihat data yang diterima dicetak di konsol.**