import sqlite3

def create_connection():
    return sqlite3.connect("manage.db")

def create_table():
    conn = create_connection()
    a = conn.cursor()
    a.execute('''
        CREATE TABLE IF NOT EXISTS books 
        (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT NOT NULL,
        writer_name TEXT NOT NULL,
        language TEXT NOT NULL, 
        price REAL NOT NULL)
    ''')
    conn.commit()
    conn.close()

def add_book(book_name, writer_name, language, price):
    conn = create_connection()
    a = conn.cursor()
    a.execute('INSERT INTO books (book_name, writer_name, language, price) VALUES (?, ?, ?, ?)',
              (book_name, writer_name, language, price))
    conn.commit()
    conn.close()

def show_books():
    conn = create_connection()
    a = conn.cursor()
    a.execute('SELECT * FROM books')
    rows = a.fetchall()
    for row in rows:
        print(row)
    conn.close()

def edit_book(book_id, book_name, writer_name, language, price):
    conn = create_connection()
    a = conn.cursor()
    a.execute('UPDATE books SET book_name = ?, writer_name = ?, language = ?, price = ? WHERE book_id = ?',
              (book_name, writer_name, language, price, book_id))
    conn.commit()
    conn.close()

def search_book(book_name, writer_name):
    conn = create_connection()
    a = conn.cursor()
    a.execute("SELECT * FROM books WHERE book_name = ? OR writer_name = ?",
              (book_name, writer_name))
    results = a.fetchall()
    for row in results:
        print(row)
    conn.close()

def main():
    create_table()

    while True:
        print("Library menu: ")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Edit Book")
        print("4. Search Book")

        choice = input("Enter your Choice: ")

        if choice == '1':
            book_name = input("Enter Book Name: ")
            writer_name = input("Enter Writer Name: ")
            language = input("Enter Language: ")
            price = input("Enter Price: ")
            add_book(book_name, writer_name, language, price)
        elif choice == '2':
            show_books()
        elif choice == '3':
            book_id = int(input("Enter Book ID to update: "))
            book_name = input("Enter new Book Name: ")
            writer_name = input("Enter new Writer Name: ")
            language = input("Enter Book Language: ")
            price = input("Enter new Price: ")
            edit_book(book_id, book_name, writer_name, language, price)
        elif choice == '4':
            book_name = input("Enter Book Name: ")
            writer_name = input("Enter Writer Name: ")
            search_book(book_name, writer_name)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
