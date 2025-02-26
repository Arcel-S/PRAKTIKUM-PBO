Height = int(input("Masukkan tinggi segitiga: "))
for i in range(1, Height + 1): 
    print(' ' * (Height - i) + '*' * (2 * i - 1))