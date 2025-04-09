# Define a class

class Student:
    def __init__(self, name, age, college):
        self.name = input("Enter student Name: ")
        self.age = input("Enter Student Age: ")
        self.college = input("Enter the College Name: ")


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"College Name: {self.college}")

student_list = []
student_list.append(Student(["self.name"], ["self.age"], ["self.college"]))

for student in student_list:
    print(student_list)
    student.display_info()