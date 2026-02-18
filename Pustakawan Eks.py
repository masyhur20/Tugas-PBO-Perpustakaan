### SIMULASI PERPUSTAKAAN SEDERHANA ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B         

from Pustakawan import Buku, Pengunjung, Pustakawan

# Kelas Buku
buku_1 = Buku("Si Anak Pemberani", "Tere Liye", "PT. Sabak Grip Nusantara", 2024, "Depok", "Novel", 435)
buku_2 = Buku("Negeri 5 Menara", "Ahmad Fuadi", "PT. Gramedia Pustaka Utama", 2009, "Jakarta", "Novel", 423)
buku_3 = Buku("Tenggelamnya Kapal van der Wijck", "Hamka", "PT. Bulan Bintang", 1938, "Jakarta", "Novel", 224)
buku_4 = Buku("5 cm", "Donny Dirgantoro", "Grasindo", 2005, "Jakarta", "Novel", 381)
buku_5 = Buku("Laut Bercerita", "Leila S. Chudori", "PT. Kepustakaan Populer Gramedia", 2017, "Jakarta", "Novel", 394)


# Kelas Pengunjung
Pengunjung_1 = Pengunjung("Muhammad", "12500000001", "Dakwah & Ilmu Komunikasi", "Manajemen Dakwah")
Pengunjung_2 = Pengunjung("Musthofa", "12500000002", "Tarbiyah & Keguruan", "Pendidikan Agama Islam")
Pengunjung_3 = Pengunjung("Masyhur", "12500000003", "Sains & Teknologi", "Teknik Informatika")

print(" ")
print("== IDENTITAS PENGUNJUNG ==")
print(Pengunjung_1)
print(Pengunjung_2)
print(Pengunjung_3)


# Kelas Pustakawan
Pustakawan_1 = Pustakawan("Rohman")
Pustakawan_2 = Pustakawan("Rohim")

## Proses Tambah dan Hapus Buku
Pustakawan_1.tambah_buku(buku_1)
Pustakawan_1.tambah_buku(buku_2)
Pustakawan_1.tambah_buku(buku_4)

#Pustakawan_1.hapus_buku(buku_1)

## Proses menampilkan list buku
Pustakawan_1.tampilkan_list_buku()

## Proses peminjaman dan pengembalian buku
Pustakawan_1.peminjaman(Pengunjung_1, buku_4)
#Pustakawan_1.peminjaman(Pengunjung_1, buku_4)
Pustakawan_1.pengembalian(Pengunjung_2, buku_4)
#Pustakawan_2.pengembalian(Pengunjung_2, buku_5)
#Pustakawan_1.peminjaman(Pengunjung_2, buku_4)