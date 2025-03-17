import tkinter as tk
from tkinter import messagebox
import math

class Kalkulator:
    def __init__(self, angka):
        self.angka = angka
    
    def __add__(self, other):
        return Kalkulator(self.angka + other.angka)
    
    def __sub__(self, other):
        return Kalkulator(self.angka - other.angka)
    
    def __mul__(self, other):
        return Kalkulator(self.angka * other.angka)
    
    def __truediv__(self, other):
        if other.angka == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        return Kalkulator(self.angka / other.angka)
    
    def __pow__(self, other):
        return Kalkulator(self.angka ** other.angka)
    
    def log(self):
        if self.angka <= 0:
            raise ValueError("Logaritma hanya untuk angka positif!")
        return Kalkulator(math.log(self.angka))
    
    def __str__(self):
        return str(round(self.angka, 4))  # Hasil lebih rapi dengan pembulatan

# Fungsi operasi
def hitung(operasi):
    try:
        a = Kalkulator(float(entry_a.get()))
        
        if operasi == 'log':
            hasil = a.log()
        else:
            b = Kalkulator(float(entry_b.get()))
            if operasi == '+':
                hasil = a + b
            elif operasi == '-':
                hasil = a - b
            elif operasi == '*':
                hasil = a * b
            elif operasi == '/':
                hasil = a / b
            elif operasi == '^':
                hasil = a ** b
        
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI menggunakan Tkinter
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Input angka
tk.Label(root, text="Masukkan nilai a:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Masukkan nilai b:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

# Tombol operasi
frame = tk.Frame(root)
frame.grid(row=2, columnspan=2)

opsi = ['+', '-', '*', '/', '^', 'log']
for i, op in enumerate(opsi):
    tk.Button(frame, text=op, command=lambda op=op: hitung(op)).grid(row=0, column=i)

# Label hasil
label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.grid(row=3, columnspan=2)

root.mainloop()
