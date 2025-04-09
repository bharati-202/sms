import sqlite3

# Create or connect to a database
conn = sqlite3.connect("contact.db")
cursor = conn.cursor()

# Create a table for Contacts

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL,
phone INTEGER NOT NULL, 
email TEXT NOT NULL)
''')

# Function to add a new contact
def add_contact(name, phone, email):
    cursor.execute('''
    INSERT INTO contacts (name, phone email) VALUES (?, ?, )''')


