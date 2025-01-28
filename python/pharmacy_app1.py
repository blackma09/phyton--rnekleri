# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:56:54 2024

@author: ENES
"""
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eczane Yönetim Sistemi")
        
        # Tema ve arka plan rengi ekleme
        self.style = ttk.Style()
        self.style.theme_use('clam')  # 'clam', 'alt', 'default', 'classic' gibi çeşitli temalar kullanılabilir
        self.root.configure(background='#ffcccc')  # Arka plan kırmızı renk
        
        self.medicines = []
        
        self.label_name = ttk.Label(root, text="İlaç Adı:", background='#ffcccc')
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        
        self.entry_name = ttk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_price = ttk.Label(root, text="Fiyat:", background='#ffcccc')
        self.label_price.grid(row=1, column=0, padx=10, pady=5)
        
        self.entry_price = ttk.Entry(root)
        self.entry_price.grid(row=1, column=1, padx=10, pady=5)
        
        self.label_quantity = ttk.Label(root, text="Adet:", background='#ffcccc')
        self.label_quantity.grid(row=2, column=0, padx=10, pady=5)
        
        self.entry_quantity = ttk.Entry(root)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=5)
        
        self.label_buyer = ttk.Label(root, text="Satın Alan:", background='#ffcccc')
        self.label_buyer.grid(row=3, column=0, padx=10, pady=5)
        
        self.entry_buyer = ttk.Entry(root)
        self.entry_buyer.grid(row=3, column=1, padx=10, pady=5)
        
        self.label_avg_price = ttk.Label(root, text="Ortalama Fiyat (İnternet):", background='#ffcccc')
        self.label_avg_price.grid(row=4, column=0, padx=10, pady=5)
        
        self.entry_avg_price = ttk.Entry(root)
        self.entry_avg_price.grid(row=4, column=1, padx=10, pady=5)
        
        self.button_add = ttk.Button(root, text="Ekle", command=self.add_medicine)
        self.button_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.button_show = ttk.Button(root, text="İlaçları Göster", command=self.show_medicines)
        self.button_show.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.listbox_medicines = tk.Listbox(root, width=80)
        self.listbox_medicines.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    
    def add_medicine(self):
        name = self.entry_name.get()
        price = self.entry_price.get()
        quantity = self.entry_quantity.get()
        buyer = self.entry_buyer.get()
        avg_price = self.entry_avg_price.get()
        
        if name and price and quantity and buyer and avg_price:
            self.medicines.append((name, price, quantity, buyer, avg_price))
            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
            self.entry_buyer.delete(0, tk.END)
            self.entry_avg_price.delete(0, tk.END)
            messagebox.showinfo("Bilgi", "İlaç başarıyla eklendi!")
        else:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
    
    def show_medicines(self):
        self.listbox_medicines.delete(0, tk.END)
        for medicine in self.medicines:
            self.listbox_medicines.insert(tk.END, f"İlaç Adı: {medicine[0]}, Fiyat: {medicine[1]} TL, Adet: {medicine[2]}, Satın Alan: {medicine[3]}, Ortalama Fiyat (İnternet): {medicine[4]} TL")

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()