Tugas Backend 1 CB243

Studi Kasus 1
Studi kasus ini memodelkan entitas:
a. Address
b. Person
c. Student (turunan Person)
d. Professor (turunan Person)

Relasi penting :
a. Professor dapat membimbing (supervise) hingga maksimal 5 mahasiswa
b. Student dapat memiliki banyak supervisor
c. Person dapat memiliki alamat (Address) sebagai komposisinya

Fitur utama:
a. Validasi alamat
b. Pembelian kartu parkir oleh Person
c. Cek eligibility mahasiswa untuk mendaftar program.
d. Menambahkan supervise dan supervisor

Studi Kasus 2
Studi kasus ini memodelkan entitas:
a. LibraryItem (kelas dasar)
b. Book (turunan LibraryItem)
c. Author
d. LibraryMember

Relasi penting :
a. Setiap Book memiliki tepat satu Author

Fitur Utama :
a. Perhitungan denda keterlambatan:
    - LibraryItem -> 0.5 per hari
    - Book -> 1.0 per hari
b. Anggota perpustakaan dapat meminjam dan mengembalikan item
c. Buku memiliki penulis (komposisi)

Cara Menjalankan Program
a. Studi Kasus 1
    cd studi_kasus_1
    python main.py

b. Studi Kasus 2
    cd studi_kasus_2
    python main.py

Asumsi Impelentasi
a. Maksimal supervisee per professor adalah 5 (menyesuaikan dengan diagram)
b. Jumlah seminar mahasiswa berdasarkan formula sederhana yaitu average_mark // 10
c. Denda buku berbeda dari item perpustakaan biasa hanya mengasumsikan angka tertentu agar konsep OOP (override) dapat berjalan
d. Validasi alamat hanya memeriksa string kosong dan kode pos > 0.

Dokumentasi Penggunaan AI :
a. Model AI ChatGPT digunakan untuk membantu penyusunan struktur kode, dokumentasi, dan contoh output.