import math

def hitung_akar():
    while True:
        try:
            angka = input("Masukkan angka: ")
            angka = float(angka)
            
            if angka < 0:
                raise ValueError("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                raise ValueError("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            
            hasil = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {hasil}")
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

hitung_akar()
