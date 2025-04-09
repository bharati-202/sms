import sqlite3

# Database connection
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Table creation
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL, 
age INTEGER NOT NULL,
grade TEXT NOT NULL)
''')
conn.commit()


# Create: Add a new student
def add_student(name, age, grade):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (?,?,?)', (name, age, grade))
    conn.commit()
    print("Student added successfully!")

# Read: Fetch all student data
def view_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update: Modify student data
def update_student(student_id , name, age, grade):
    cursor.execute('''
    UPDATE students SET name=?, age=?, grade=? WHERE id=?''', (name, age, grade, student_id))
    conn.commit()
    print("Student updated successfully!")

#Delete: Remove student data
def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    print("Student deleted successfully!")

#Main menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        add_student(name, age, grade)
    elif choice == '2':
        view_students()
    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        update_student(student_id, name, age, grade)
    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again!")

#Close connection
conn.close()




