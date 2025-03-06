class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        print(f"Jenis Kendaraan   : {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")
    
    def bergerak(self):
        print(f"Kendaraan {self.jenis} sedang bergerak")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        self.info_kendaraan()
        print(f"Merk        : {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")
    
    def bunyikan_klakson(self):
        print(f"Mobil {self.merk} berbunyi: Geser! Geser!")

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga
    
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        self.__harga = value
    
    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda : {self.__tenaga_kuda} HP")
        print(f"Harga       : Rp {self.__harga} juta")
    
    def mode_balap(self):
        print(f"Mobil Sport {self.merk} telah masuk mode balap!")


ferrari = MobilSport("Sport", 340, "Ferrari", 2, 670, 8500)

ferrari.info_mobil_sport()
ferrari.bergerak()
ferrari.bunyikan_klakson()
ferrari.mode_balap()

ferrari.set_tenaga_kuda(700)
ferrari.set_harga(9000)
print(f"Tenaga Kuda baru: {ferrari.get_tenaga_kuda()} HP")
print(f"Harga baru: Rp {ferrari.get_harga()} juta")
