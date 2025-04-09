import random
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.num_correct = 0

    def run_quiz(self):
        for num, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {num}:")
            self.num_correct += self.ask_question(question)
        print(f"\nYou got {self.num_correct} correct out of {len(self.questions)} questions")

    def ask_question(self, question):
        correct_answers = set(question["answers"])
        alternatives = question["answers"] + question["alternatives"]
        ordered_alternatives = random.sample(alternatives, k=len(alternatives))
        answers = set(self.get_answers(question["question"], ordered_alternatives, len(correct_answers), question.get("hint")))
        if answers == correct_answers:
            print("⭐ Correct! ⭐")
            return 1
        else:
            print(f"No, the correct answer{' is' if len(correct_answers) == 1 else 's are'}: {', '.join(correct_answers)}")
            if "explanation" in question:
                print(f"\nEXPLANATION:\n{question['explanation']}")
            return 0

    def get_answers(self, question, alternatives, num_choices=1, hint=None):
        print(f"{question}?")
        labeled_alternatives = {chr(97 + i): alt for i, alt in enumerate(alternatives)}
        if hint:
            labeled_alternatives["?"] = "Hint"
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")
        while True:
            answer = input(f"\nChoice{'s' if num_choices > 1 else ''} (choose {num_choices})? ").replace(",", " ").split()
            if hint and "?" in answer:
                print(f"\nHINT: {hint}")
                continue
            if len(answer) == num_choices and all(a in labeled_alternatives for a in answer):
                return [labeled_alternatives[a] for a in answer]
            print(f"Invalid choice. Please choose {num_choices} valid option{'s' if num_choices > 1 else ''}.")

def prepare_questions():
    questions = [
        {
            "question": "Which function in the provided code is responsible for preparing the questions for the quiz?",
            "answers": ["prepare_questions()"],
            "alternatives": ["run_quiz()", "ask_question()", "get_answers()"],
            "hint": "It's the function that loads and selects the questions.",
            "explanation": "The prepare_questions() function is responsible for loading the questions from a file and selecting a subset of them for the quiz."
        },
        # Add more questions here
    ]
    return questions

if __name__ == "__main__":
    questions = prepare_questions()
    quiz = Quiz(questions)
    quiz.run_quiz()
