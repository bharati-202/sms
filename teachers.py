class Classroom:
    def __init__(self):
        self.teacher_data = {
            "junior teacher": {
                "Ramu": "Physics",
                "Shamu": "Mathematics",
                "Mamu": "Marathi",
                "Kitanu": "Hindi"
            },
            "senior teacher": {
                "Janak": "MBA",
                "Kanak": "B.Tech",
                "Zamak": "M.Tech",
                "Sanak": "B.Sc"
            }
        }

    def showing_data(self, teachers):
        return self.teacher_data.get(teachers, "Teachers data not found.")

data = Classroom()

while True:
    position = input("Enter Level (junior teacher/senior teacher): ")
    if position in data.teacher_data:
        print(data.teacher_data[position])
        specific_subject = input("Do you want to know specific subject (yes/no): ")
        if specific_subject == "yes":
            teacher = input("Enter Teacher name: ")
            while True:
                if teacher in data.teacher_data[position]:
                    print(f"{teacher} teaches {data.teacher_data[position][teacher]}")
                else:
                    print("Teacher not found.")
        else:
            print("OK")
    else:
        print("Level not found.")
