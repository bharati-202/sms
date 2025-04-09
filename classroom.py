
class Classroom:
    print("\nFutureTech Computers")
    def __init__(self):
        self.classdata = {
            "Raman" : {
                "Course" : "Java",
                "Fees" : "5000",
                "Timing" : "11Am to 1Pm"
            },
            "Chhagan" : {
                "Course" : "Python",
                "Fees" : "5000",
                "Timing" : "1PM to 4PM"
            },
            "Baban" : {
                "Course" : "C++",
                "Fees" : "4000",
                "Timing" : "10AM to 12PM"
            }

        }
    def students(self, user_input):
        return self.classdata.get(user_input, "Student data does not exist.")

data = Classroom()

while True:
    user_input = input("Enter student name: ")
    print(data.classdata[user_input])
    print(data.classdata["Raman"]["Timing"])

