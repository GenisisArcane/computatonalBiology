from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, static_folder='static')

def get_db_connection():
    conn = sqlite3.connect('specimens.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS specimens
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  specimen_size REAL,
                  magnification INTEGER,
                  actual_size REAL)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    actual_size = None
    error = None
    
    if request.method == 'POST':
        try:
            username = request.form['username']
            specimenSize = float(request.form['microscope_size'])
            magnification = int(request.form['magnification'])
            
            actualSize = specimenSize / magnification * 1000
            
            conn = get_db_connection()
            conn.execute("INSERT INTO specimens (username, specimen_size, magnification, actual_size) VALUES (?, ?, ?, ?)",
                         (username, specimenSize, magnification, actualSize))
            conn.commit()
            conn.close()
            
        except ValueError as e:
            error = "Please enter valid numbers"
        except Exception as e:
            error = "An error occurred"
    
    conn = get_db_connection()
    specimens = conn.execute('SELECT * FROM specimens ORDER BY id DESC').fetchall()
    conn.close()
    
    return render_template('index.html', 
                         actual_size=actual_size,
                         specimens=specimens,
                         error=error)

if __name__ == '__main__':
    app.run(debug=True)