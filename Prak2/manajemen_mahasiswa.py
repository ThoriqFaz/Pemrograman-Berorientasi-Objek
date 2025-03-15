#Nama : Muhammad Thoriq Fairusazulfa
#NIM : 23.01.4970
#Kelas : D3TI01

import json
import os

class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}")

class ManajemenMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, nama, nim, prodi):
        if self.cari_mahasiswa(nim) is None:
            mahasiswa = Mahasiswa(nama, nim, prodi)
            self.daftar_mahasiswa.append(mahasiswa)
        else:
            print(f"Mahasiswa dengan NIM {nim} sudah ada!")

    def tampilkan_semua(self):
        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan_info()

    def ubah_mahasiswa(self, nim, nama_baru=None, prodi_baru=None):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                if nama_baru:
                    mahasiswa.nama = nama_baru
                if prodi_baru:
                    mahasiswa.prodi = prodi_baru
                print("Data berhasil diubah!")
                return
        print("Mahasiswa tidak ditemukan!")

    def hapus_mahasiswa(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                self.daftar_mahasiswa.remove(mahasiswa)
                print("Mahasiswa berhasil dihapus!")
                return
        print("Mahasiswa tidak ditemukan!")

    def cari_mahasiswa(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def simpan_ke_file(self, nama_file):
        data = [{'nama': mhs.nama, 'nim': mhs.nim, 'prodi': mhs.prodi} for mhs in self.daftar_mahasiswa]
        with open(nama_file, 'w') as file:
            json.dump(data, file)
        print("Data berhasil disimpan ke file!")

    def baca_dari_file(self, nama_file):
        if not os.path.exists(nama_file):
            with open(nama_file, 'w') as file:
                json.dump([], file)
            print("File tidak ditemukan, membuat file baru!")
        else:
            with open(nama_file, 'r') as file:
                data = json.load(file)
                self.daftar_mahasiswa = [Mahasiswa(mhs['nama'], mhs['nim'], mhs['prodi']) for mhs in data]
            print("Data berhasil dibaca dari file!")

# Membuat objek manajemen mahasiswa
manajemen = ManajemenMahasiswa()

# Membaca data mahasiswa dari file saat program dijalankan pertama kali
manajemen.baca_dari_file('data_mahasiswa.json')

# Mengosongkan daftar mahasiswa sebelum menambah data baru
manajemen.daftar_mahasiswa = []

# Menambah mahasiswa hanya jika belum ada
mahasiswa_baru = [
    ("Diahiro", "23014958", "Teknik Informatika"),
    ("Thoriq", "23014970", "Teknik Informatika"),
    ("Habib", "23014974", "Teknik Informatika"),
    ("Naufal", "23014975", "Teknik Informatika"),
    ("Neferal", "23014990", "Teknik Informatika"),
    ("Maritza", "23015000", "Teknik Informatika"),
    ("Arya", "23015003", "Teknik Informatika")
]

for nama, nim, prodi in mahasiswa_baru:
    manajemen.tambah_mahasiswa(nama, nim, prodi)

# Menyimpan data mahasiswa ke dalam file
manajemen.simpan_ke_file('data_mahasiswa.json')

# Menampilkan semua mahasiswa
print("\nDaftar Mahasiswa:")
manajemen.tampilkan_semua()

# Mencari mahasiswa berdasarkan NIM
mahasiswa = manajemen.cari_mahasiswa("23014970")
if mahasiswa:
    mahasiswa.tampilkan_info()
else:
    print("Mahasiswa tidak ditemukan!")
