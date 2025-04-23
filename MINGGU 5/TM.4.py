import tkinter as tk
from tkinter import messagebox, Menu, Scrollbar, END, Frame
from datetime import datetime
import json
import os

class CatatanHarianApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        self.catatan = {}
        self.judul_terpilih = None

        self.buat_menu()
        self.buat_widget()
        self.muat_dari_file()

    def buat_menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Keluar", command=self.keluar_aman)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tentang", command=lambda: messagebox.showinfo("Tentang", "Catatan Harian v1.0"))
        menubar.add_cascade(label="Bantuan", menu=helpmenu)

        self.root.config(menu=menubar)

    def buat_widget(self):
        frame_atas = Frame(self.root, padx=10, pady=10)
        frame_atas.grid(row=0, column=0, columnspan=2, sticky='we')

        tk.Label(frame_atas, text="Judul:", font=("Arial", 10)).grid(row=0, column=0, sticky='w')
        self.entry_judul = tk.Entry(frame_atas, width=40, font=("Arial", 10))
        self.entry_judul.grid(row=0, column=1, padx=5, sticky='we')

        tk.Button(frame_atas, text="Buat Catatan Baru", command=self.mulai_catatan_baru).grid(row=1, column=0, pady=5)
        tk.Button(frame_atas, text="Tambah Catatan", command=self.tambah_catatan).grid(row=1, column=1, sticky='w')
        tk.Button(frame_atas, text="Edit Catatan", command=self.edit_catatan).grid(row=1, column=1, sticky='e', padx=(0, 100))
        tk.Button(frame_atas, text="Hapus Catatan", command=self.hapus_catatan).grid(row=1, column=1, sticky='e')

        frame_bawah = Frame(self.root, padx=10, pady=5)
        frame_bawah.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.listbox = tk.Listbox(frame_bawah, width=40, font=("Arial", 10))
        self.listbox.grid(row=0, column=0, sticky='ns')
        self.listbox.bind('<<ListboxSelect>>', self.tampilkan_catatan)

        scrollbar = Scrollbar(frame_bawah, command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.text_isi = tk.Text(frame_bawah, font=("Arial", 10), wrap='word', state='disabled')
        self.text_isi.grid(row=0, column=2, sticky='nsew', padx=(10, 0))
        frame_bawah.grid_columnconfigure(2, weight=1)
        frame_bawah.grid_rowconfigure(0, weight=1)

    def mulai_catatan_baru(self):
        self.entry_judul.delete(0, END)
        self.text_isi.config(state='normal')
        self.text_isi.delete("1.0", END)
        self.judul_terpilih = None

    def tambah_catatan(self):
        judul = self.entry_judul.get().strip()
        self.text_isi.config(state='normal')
        isi = self.text_isi.get("1.0", END).strip()

        if not judul or not isi:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong.")
            return

        if judul in self.catatan and self.judul_terpilih is None:
            messagebox.showerror("Error", "Judul catatan sudah ada.")
            return

        waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.catatan[judul] = {
            "isi": isi,
            "waktu": waktu
        }

        if self.judul_terpilih and self.judul_terpilih != judul:
            del self.catatan[self.judul_terpilih]

        self.perbarui_listbox()
        self.entry_judul.delete(0, END)
        self.text_isi.delete("1.0", END)
        self.text_isi.config(state='disabled')
        self.judul_terpilih = None

    def tampilkan_catatan(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            teks = self.listbox.get(index)
            waktu, judul = teks.split("] ", 1)
            self.judul_terpilih = judul
            isi = self.catatan[judul]["isi"]
            self.entry_judul.delete(0, END)
            self.entry_judul.insert(0, judul)
            self.text_isi.config(state='normal')
            self.text_isi.delete("1.0", END)
            self.text_isi.insert(END, isi)
            self.text_isi.config(state='disabled')

    def hapus_catatan(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            teks = self.listbox.get(index)
            waktu, judul = teks.split("] ", 1)
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus catatan '{judul}'?")
            if konfirmasi:
                self.listbox.delete(index)
                self.catatan.pop(judul, None)
                self.text_isi.config(state='normal')
                self.text_isi.delete("1.0", END)
                self.text_isi.config(state='disabled')
                self.entry_judul.delete(0, END)
                self.judul_terpilih = None

    def edit_catatan(self):
        if self.judul_terpilih:
            self.text_isi.config(state='normal')
        else:
            messagebox.showinfo("Info", "Pilih catatan yang ingin diedit.")

    def perbarui_listbox(self):
        self.listbox.delete(0, END)
        for judul, data in self.catatan.items():
            label = f"[{data['waktu']}] {judul}"
            self.listbox.insert(END, label)

    def muat_dari_file(self):
        if os.path.exists("data_catatan.json"):
            try:
                with open("data_catatan.json", "r") as f:
                    self.catatan = json.load(f)
                self.perbarui_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat catatan: {e}")

    def simpan_ke_file(self):
        try:
            with open("data_catatan.json", "w") as f:
                json.dump(self.catatan, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan catatan: {e}")

    def keluar_aman(self):
        self.simpan_ke_file()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("780x450")
    app = CatatanHarianApp(root)

    def on_closing():
        app.simpan_ke_file()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    
