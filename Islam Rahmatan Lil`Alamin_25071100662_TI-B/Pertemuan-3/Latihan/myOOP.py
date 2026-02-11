class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga
        
    def info_produk(self):
        print(f"Produk {self.nama_produk} memiliki harga: {self.harga}")
        return self.nama_produk, self.harga
    
class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        
        self.garansi = garansi
        
    def info_produk(self):
        print(f"Produk {self.nama_produk} memiliki harga: {self.harga} dengan garansi {self.garansi} tahun")
        return self.nama_produk, self.harga, self.garansi
    
class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        
        self.tanggal_kadaluarsa = tanggal_kadaluarsa
        
    def info_produk(self):
        print(f"Produk {self.nama_produk} memiliki harga: {self.harga} dengan tanggal_kadaluarsa {self.tanggal_kadaluarsa}")
        return self.nama_produk, self.harga, self.tanggal_kadaluarsa
    
tivi = ProdukElektronik("TV", 3000000, 2)
roti = ProdukMakanan("Roti", 15000, "12-12-2026")

tivi.info_produk()
roti.info_produk()



#============================================================================#
#============================================================================#
##                             Plymorphism
#============================================================================#
#============================================================================#

class Notifikasi:
    def kirim(self):
        print("halo dunia")
        
class Email(Notifikasi):
    def kirim(self):
        print("Pesan dikirim melalui email")
        
class SMS(Notifikasi):
    def kirim(self):
        print("Pesan dikirim melalui sms")
        
hp1 = Notifikasi()
hp2 = Email()
hp3 = SMS()

hp1.kirim()
hp2.kirim()
hp3.kirim()


#============================================================================#
#============================================================================#
##                             Encapsulation
#============================================================================#
#============================================================================#

class Mahasiswa:
    def __init__(self, nilai):
        self.__nilai = nilai
        
    def setNilai(self, nilaiBaru):
        self.__nilai = nilaiBaru
        
    def getNilai(self):
        if self.__nilai >= 0 and self.__nilai <= 100:
            print(self.__nilai)
            return self.__nilai
        print("nilai tidak valid")
        
alam = Mahasiswa(100)
akil = Mahasiswa(200)
ilyas = Mahasiswa(-1)

alam.getNilai()
akil.getNilai()
ilyas.getNilai()

alam.setNilai(27)
alam.getNilai()


