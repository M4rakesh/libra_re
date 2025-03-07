import tkinter as tk
from tkinter import messagebox
import re

def paarbaude_vaardu():
    vaards = vaards_entry.get()
    pattern = r'^[A-Z]{1}[a-z]{1,}'
    
    if re.match(pattern, vaards):
        messagebox.showinfo("Rezultāts", "Vards ir derīga!")
    else:
        messagebox.showerror("Rezultāts", "Vārds nav derīga!")

root = tk.Tk()
root.title("Vārda pārbaude")

tk.Label(root, text="Ievadiet vārdu:").pack(pady=5)
vaards_entry = tk.Entry(root, width=30)
vaards_entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_vaardu).pack(pady=5)

root.mainloop()
