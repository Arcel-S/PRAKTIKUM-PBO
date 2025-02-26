#Solusi
banyak_siswa = int(input("Masukkan jumlah siswa: "))
dataSiswa = {}

for i in range(banyak_siswa):
    nama = input(f"Masukkan nama siswa ke-{i + 1}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    dataSiswa[nama] = nilai

print("dict =", dataSiswa)  