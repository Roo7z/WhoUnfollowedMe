# WhoUnfollowedMe

**WhoUnfollowedMe** adalah script sederhana yang membantu Anda melacak siapa saja yang berhenti mengikuti (unfollow) akun Instagram Anda. Dengan menggunakan script ini, Anda dapat mengetahui perubahan pada daftar pengikut (followers) secara efisien.

## 📋 Fitur
- Melacak pengguna yang berhenti mengikuti akun Anda.
- Menyimpan data pengikut untuk analisis lebih lanjut.
- Output yang mudah dipahami.
- Kompatibel dengan berbagai platform (Python-based).

## 📦 Persyaratan
Pastikan Anda memiliki:
- Python 3.8 atau lebih baru
- Library berikut:
  - `json`

## 🚀 Instalasi
1. Clone repo ini ke perangkat Anda:
   ```bash
   git clone https://github.com/username/WhoUnfollowedMe.git
   cd WhoUnfollowedMe
   ```

## 📂 Tutorial: Mengunduh Data Informasi Pribadi dari Instagram
Untuk menjalankan script ini, Anda memerlukan data pengikut Anda. Berikut cara mengunduhnya langsung dari Instagram:

1. **Masuk ke akun Instagram Anda** melalui aplikasi atau browser.
2. **Buka pengaturan privasi**:
   - Klik ikon profil Anda.
   - Pilih **Settings** (Pengaturan) > **Privacy and Security** (Privasi dan Keamanan).
3. **Unduh data Anda**:
   - Cari opsi **Data Download** (Unduhan Data).
   - Klik **Request Download** (Minta Unduhan).
   - Masukkan alamat email Anda dan pilih format **JSON**.
4. **Konfirmasi permintaan**:
   - Instagram akan mengirimkan email berisi tautan untuk mengunduh data Anda.
   - Klik tautan dalam email tersebut dan unduh file ZIP.
5. **Ekstrak data**:
   - Ekstrak file ZIP untuk mendapatkan folder yang berisi berbagai file JSON, termasuk daftar pengikut Anda (`followers.json`).

Setelah data diunduh, pindahkan file `followers.json` ke folder tempat script ini berada.

## 🔧 Penggunaan
1. Jalankan script untuk mengambil daftar pengikut saat ini:
   ```bash
   python who_unfollowed_me.py
   ```
2. Script akan membandingkan daftar pengikut terbaru dengan data sebelumnya untuk menunjukkan siapa saja yang telah unfollow.


## 🤝 Kontribusi
Saya terbuka untuk kontribusi! Jika Anda memiliki ide atau perbaikan, silakan fork repo ini dan buat pull request.

## ✨ Dukungan
Jika Anda merasa script ini berguna, beri bintang pada repo ini ⭐ atau kirimkan saran Anda melalui [Issues](https://github.com/username/WhoUnfollowedMe/issues).
