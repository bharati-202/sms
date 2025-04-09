class ChatBot:
    def __init__(self):
        self.responses = {
            "hello" : "Hi! How can I assist you today?",
            "How are you?" : "I'm just a program, but I'm here to help you!",
            "What is your name": "I'm Chatbot, your virtual assistant.",
            "bye" : "Goodbye! Have a great day!"
        }
    def get_responses(self, user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")

bot = ChatBot()

print("ChatBot: hello! you can ask me something (type 'bye' to exit).")
while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: ", bot.get_responses("bye"))
            break
        response = bot.get_response(user_input)
        print("ChatBot: ", response)
