### SIMULASI PERPUSTAKAAN SEDERHANA ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B         

# Kelas Buku
class Buku:
    def __init__(self, judul, penulis, penerbit, tahun, kota, tipe, halaman):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun = tahun
        self.kota = kota
        self.tipe = tipe
        self.halaman = halaman
        self.peminjam = None


# Kelas Pengunjung  
class Pengunjung:
    def __init__(self, nama, nim, fakultas, jurusan):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.jurusan = jurusan

    def __str__(self):
        return (f"\n{'Nama':<10} : {self.nama}\n"
                f"{'NIM':<10} : {self.nim}\n"
                f"{'Fakultas':<10} : {self.fakultas}\n"
                f"{'Jurusan':<10} : {self.jurusan}")
    
# Kelas Pustakawan
class Pustakawan:
    def __init__(self, nama_petugas):
        self.nama = nama_petugas
        self.list_buku = []

    def tambah_buku(self,buku_baru):
        self.list_buku.append(buku_baru)
        print(f"\nBuku '{buku_baru.judul}' berhasil ditambahkan kedalam list buku!!")

    def hapus_buku(self,buku_rusak):
        if buku_rusak in self.list_buku:
            self.list_buku.remove(buku_rusak)
            print(f"\nBuku '{buku_rusak.judul}' berhasil dihapus dari list buku!!")
        
        else:
            print(f"Gagal menghapus!! Buku tidak ditemukan didalam list")

    def tampilkan_list_buku(self):
        print(f"\n--- LIST BUKU PERPUSTAKAAN ---\n")

        for b in self.list_buku:
            print(f"- {b.judul} - {b.penulis} ({b.tahun})")

    def peminjaman(self, peminjam, buku):
        print(" ")
        print("Mengecek Status...")
        print(" ")

        if buku not in self.list_buku:
            print("Gagal!! Buku tidak ada didalam list")
            return

        if buku.peminjam is not None:
            print(f"Maaf buku '{buku.judul}' sedang dipinjam oleh : {buku.peminjam.nama}")
            
        
        else:
            buku.peminjam = peminjam

            print(" ")
            print("=== Bukti Peminjaman Buku ===")
            print(" ")
            print(f"{'Petugas':<10} : {self.nama}")
            print(" ")
            print(f"{'Peminjam':<10} : {peminjam.nama}")
            print(f"{'NIM':<10} : {peminjam.nim}")
            print(" ")
            print(f"{'Judul Buku':<10} : {buku.judul}")
            print(f"{'Penulis':<10} : {buku.penulis}")
            print(f"{'Tahun':<10} : {buku.tahun}")
            print(" ")
            print("~~~ Peminjaman Buku Berhasil ~~~")

    def pengembalian(self, peminjam, buku):
        print(" ")
        print("Mengecek Status...")

        if buku not in self.list_buku:
            print("Gagal!! Buku tidak ada didalam list")
            return
        
        if buku.peminjam is None:
            print(" ")
            print(f"GAGAL: buku '{buku.judul}' sudah ada di rak!!")
            print("Periksa kembali judul buku yang hendak dikembalikan!!!")

        elif buku.peminjam != peminjam:
            print(f"GAGAL: Identitas tidak cocok!!!")
            print(f"Buku ini dipinjam oleh '{buku.peminjam.nama}', bukan oleh '{peminjam.nama}'")
       
        else:
            buku.peminjam = None
            print(" ")
            print("=== Bukti Pengembalian Buku ===")
            print(" ")
            print(f"{'Petugas':<10} : {self.nama}")
            print(" ")
            print(f"{'Peminjam':<10} : {peminjam.nama}")
            print(f"{'NIM':<10} : {peminjam.nim}")
            print(" ")
            print(f"{'Judul Buku':<10} : {buku.judul}")
            print(f"{'Penulis':<10} : {buku.penulis}")
            print(f"{'Tahun':<10} : {buku.tahun}")
            print(" ")
            print("~~~ Pengembalian Buku Berhasil ~~~")