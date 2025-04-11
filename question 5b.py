import sqlite3

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


print("Microscope Specimen Size Calculator with Database")

try:
    
    username = input("Enter username: ")
    specimenSize = float(input("Enter the size observed under microscope (mm): "))
    magnification = int(input("Enter the magnification power: "))
    
    
    actualSize = specimenSize / magnification * 1000
    print(f"Actual size of the specimen: {actualSize:.2f} µm")
    
    
    conn = sqlite3.connect('specimens.db')
    c = conn.cursor()
    c.execute("INSERT INTO specimens VALUES (NULL, ?, ?, ?, ?)",
              (username, specimenSize, magnification, actualSize))
    conn.commit()
    conn.close()
    print("Data saved to database.")
    
except ValueError:
    print("Please enter valid numbers.")