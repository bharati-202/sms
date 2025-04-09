# List of students with their names, ages, and marks

students = [
    {'name' : 'Ram', 'age' : '20', 'Mathematics' : '88', 'Science' : '90', 'English' : '45'},
    {'name' : 'Sham', 'age' : '21', 'Mathematics' : '55', 'Science' : '65', 'English' : '77'},
    {'name' : 'Jaam', 'age' : '22', 'Mathematics' : '65', 'Science' : '87', 'English' : '87'},
    {'name' : 'Baam', 'age' : '23', 'Mathematics' : '88', 'Science' : '54', 'English' : '33'}
]

# Regular function to calculate total marks
def calculate_total_marks(std):
    return std['Mathematics'] + std['Science'] + std['English']

# Adding total marks to each student's record

for std in students:
    std['total_marks'] = calculate_total_marks(std)

# Lambda function to determine if a student has passed (assuming pass mark is 210 out of 300)
has_passed = lambda student: student['total_marks'] >= 210



