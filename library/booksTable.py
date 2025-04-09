import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# 1. Library Books Table

cursor.execute('''CREATE TABLE IF NOT EXISTS library (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT NOT NULL,
    writer_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price  INTEGER NOT NULL,
    language TEXT NOT NULL
    )
    ''')
conn.commit()

# 2. Customer Table

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_email TEXT UNIQUE, 
    customer_address TEXT)
    ''')
conn.commit()

# 3. Dealer Table

cursor.execute('''CREATE TABLE IF NOT EXISTS dealers(
    dealer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dealer_name TEXT NOT NULL,
    dealer_contact INTEGER,
    dealer_address TEXT)
    ''')
conn.commit()

# 4. Sales Table

cursor.execute('''CREATE TABLE IF NOT EXISTS sales(
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    book_id INTEGER,
    dealer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
    FOREIGN KEY (book_id) REFERENCE library(book_id),
    FOREIGN KEY (dealer_id) REFERENCES dealers(dealer_id)
    )
    ''')
conn.commit()

def add_book(book_name, writer_name, quantity, price, language):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO library (book_name, writer_name, quantity, price, language) VALUES (?, ?, ?, ?, ?)',
                   (book_name, writer_name,quantity, price, language))
    conn.commit()

def view_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM library')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.commit()

def update_book(book_id, book_name, writer_name, quantity, price, language):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE library SET book_name = ?, writer_name =?, quantity = ?, price = ?, language = ? WHERE book_name = ?''',
    (book_name, writer_name, quantity, price, language, book_id))
    conn.commit()

def delete_book(book_id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM library WHERE book_id = ?', (book_id))
    conn.commit()