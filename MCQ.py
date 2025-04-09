class MCQ:
    def __init__(self, questions, options, correct_options):
        self.questions = questions
        self.options = options
        self.correct_options = correct_options

    def ask(self):
        for question, option in self.questions.item():
            print(question)
            for key, value in option.item():
                print(f"{key} : {value}")
              user_answer =  input("Select an option: ")
              correct_option = [key for key, value in options.items() if value == options["Option1"]][0]
              if user_answer == correct_option:
                print("Correct!")
              else:
                print("Incorrect!")
questions = {
    "What is the capital of India?": {
       "Option1" : "Delhi",
       "Option2" : "Mumbai",
       "Option3" : "Surat",
       "Option4" : "Chennai"
    },
    "What is 2 + 2 = ?" : {
        "Option1" : 4,
        "Option2" : 5,
        "Option3" : 2,
        "Option4" : 1
    },
    "What is full form of PC?" : {
        "Option1" : "Personal Computer",
        "Option2" : "Private Computer",
        "Option3" : "Pagal Computer",
        "Option4" : "Piddi Computer"
    }

}