daftar_tugas = []  # Menyimpan daftar tugas selama program berjalan

def tambahTugas():
    print("================= TO DO LIST =================")

    while True:
        print("\nPilih Aksi: ")
        print("1. Tambah tugas")
        print("2. Hapus tugas dari daftar")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")

        try:
            pilihan = int(input('Masukkan pilihan (1 - 4): '))
        except ValueError:
            print('Pilihan harus berupa angka antara 1 hingga 4.')
            continue  # Mengulang loop jika input tidak valid

        if pilihan == 1:
            nama_tugas = input("Masukkan tugas yang ingin ditambahkan: ")
            if nama_tugas:  
                daftar_tugas.append(nama_tugas)
                print(f"Tugas '{nama_tugas}' berhasil ditambahkan.")
            else:
                print("Tugas tidak boleh kosong.")

        elif pilihan == 2:
            if not daftar_tugas:
                print("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
                continue

            try:
                hapus_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
                if 0 <= hapus_tugas < len(daftar_tugas):
                    print(f"Tugas '{daftar_tugas[hapus_tugas]}' telah dihapus.")
                    del daftar_tugas[hapus_tugas]
                else:
                    raise IndexError(f"Tidak ada tugas dengan nomor {hapus_tugas + 1}.")
            except ValueError:
                print("Inputan harus berupa angka.")
            except IndexError as e:
                print(e)

        elif pilihan == 3:
            if not daftar_tugas:
                print("Daftar tugas kosong. Silakan tambahkan tugas terlebih dahulu.")
            else:
                print("\nDaftar Tugas:")
                for i, tugas in enumerate(daftar_tugas, start=1):
                    print(f"{i}. {tugas}")

        elif pilihan == 4:
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak ada. Masukkan angka antara 1 hingga 4.")

# Jalankan program
tambahTugas()
