import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize main window
root = tk.Tk()
root.title("Microscope Specimen Calculator Application")

# Initialize database
conn = sqlite3.connect('specimens.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS specimens
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              specimen_size REAL,
              magnification INTEGER,
              actual_size REAL)''')
conn.commit()
conn.close()

# Create GUI elements
tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Specimen Size (mm):").grid(row=1, column=0, padx=5, pady=5)
size_entry = tk.Entry(root)
size_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Magnification:").grid(row=2, column=0, padx=5, pady=5)
magnification_entry = tk.Entry(root)
magnification_entry.grid(row=2, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Calculation and storage logic
def on_calculate():
    try:
        username = username_entry.get()
        specimenSize = float(size_entry.get())
        magnification = int(magnification_entry.get())
        
        actual_size = specimenSize / magnification * 1000
        result_label.config(text=f"Actual size: {actual_size:.2f} µm")
        
        # Save to database
        conn = sqlite3.connect('specimens.db')
        c = conn.cursor()
        c.execute("INSERT INTO specimens (username, specimen_size, magnification, actual_size) VALUES (?, ?, ?, ?)",
                  (username, specimenSize, magnification, actual_size))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Calculation complete and data saved!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()