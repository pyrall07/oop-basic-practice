# YouTube Mini OOP CLI Downloader

## Video Demo: url

## Description

YouTube Mini OOP CLI Downloader adalah sebuah aplikasi Command Line Interface (CLI) berbasis Python yang memungkinkan pengguna untuk mencari, menyimpan, dan mengunduh video YouTube secara interaktif. Proyek ini dibuat sebagai Proyek Akhir CS50P dan dirancang dengan pendekatan Object-Oriented Programming (OOP) agar kode mudah dipelihara, diuji, dan dikembangkan.

Aplikasi ini menggunakan library `yt-dlp` untuk melakukan pencarian dan pengunduhan video YouTube, serta `tqdm` untuk menampilkan animasi progress bar agar pengalaman pengguna di terminal lebih informatif dan bersih. Seluruh alur aplikasi dibuat modular dengan pemisahan tanggung jawab yang jelas antara layer Domain, Repository, Service, dan Infrastructure.

---

## Fitur Utama

- 🔍 **Mencari video YouTube** berdasarkan kata kunci
- 📂 **Menyimpan hasil pencarian** ke repository sementara (in-memory)
- 📃 **Menampilkan daftar video yang tersimpan**
- ⬇ **Mengunduh satu atau beberapa video sekaligus**
- 📊 **Progress bar animasi** saat proses pencarian dan pengunduhan
- 🧹 **Menghapus seluruh repository**
- 🧪 **Pengujian otomatis menggunakan pytest**

---

## Cara Menjalankan Program

Pastikan Python 3.10 atau lebih baru sudah terpasang.

1. Install dependency:

   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan Program:

   ```bash
   python project.py
   ```

3. Ikuti menu interaktif di terminal

   ```markdown
   1. Search Video
   2. List saved videos
   3. Download video
   4. Clear repository
   5. Exit
   ```

## Struktur Proyek

```graphql
project/
│
├── project.py                 # Main program & fungsi wajib CS50P
├── requirements.txt           # Daftar dependency
├── README.md                  # Dokumentasi proyek
│
├── models/
│   └── video.py               # Entitas Video
│
├── repositories/
│   └── memory_repository.py   # Penyimpanan video sementara
│
├── services/
│   ├── search_service.py      # Logika pencarian video
│   └── download_service.py    # Logika download video
│
├── infrastructure/
│   └── yt_dlp/
│       ├── client.py          # Wrapper yt-dlp
│       └── options.py         # Konfigurasi yt-dlp
│
├── utils/
│   └── cli_helper.py          # Helper CLI (clear screen, pause)
│
├── tests/
│   ├── test_cli.py
│   ├── test_search_service.py
│   ├── test_download_service.py
│   ├── test_memory_repository.py
│   └── test_video.py
│
└── test_project.py            # Test untuk fungsi wajib CS50P
```

## Fungsi Wajib CS50P

Sesuai dengan spesifikasi CS50P, proyek ini memiliki **tiga fungsi tambahan** selain `main()` yang didefinisikan langsung di `project.py`:

- search_videos(search_service, keyword, max_results)
- list_videos(repo)
- download_single_video(download_service, video, path)

## Desain & Pertimbangan Teknis

- **Object-Oriented Programming (OOP)** digunakan untuk memisahkan tanggung jawab setiap komponen.
- **Dependency Injection** diterapkan agar kode mudah diuji tanpa koneksi internet.
- **pytest + pytest-mock** digunakan untuk memastikan semua fitur dapat diuji secara otomatis.
- **Progress bar bersifat visual saja**, sehingga tidak mengganggu logika bisnis dan aman saat testing.
- Repository dibuat in-memory untuk kesederhanaan dan kecepatan.
  
## Hasil yang Diharapkan

- Program dapat dijalankan sepenuhnya dari terminal
- Semua test berhasil dijalankan dengan:
  
  ```bash
  pytest -v
  ```

- Kode mudah dibaca, modular, dan siap dikembangkan lebih lanjut

## Catatan Penutup

Proyek ini dibuat sebagai sarana latihan penerapan Python, OOP, dan automated testing dalam satu aplikasi nyata. Kedepannya, aplikasi ini dapat dikembangkan dengan fitur tambahan seperti penyimpanan permanen, konfigurasi kualitas video, atau antarmuka grafis.

Terima Kasih telah meninjau proyek ini!
