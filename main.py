
from datetime import datetime

def chat():
    print("Hello! I am Nova, your personal assistant.")
    print("Type 'bye' to stop chatting.")

    while True:
        user = input("You: ").lower().strip()

        if user == "bye":
            print("Nova: Goodbye! Have a nice day!")
            break

        elif user == "hello" or user == "hi":
            print("Nova: Hello! How can I help you?")

        elif user == "how are you":
            print("Nova: I am fine! Thank you.")

        elif user == "what is your name":
            print("Nova: My name is Nova.")

        elif user == "who created you":
            print("Nova: I was created using Python.")

        elif user == "what is python":
            print("Nova: Python is a programming language.")

        elif user == "time":
            time = datetime.now().strftime("%I:%M %p")
            print("Nova: Current time is", time)

        elif user == "date":
            date = datetime.now().strftime("%d-%m-%Y")
            print("Nova: Today's date is", date)

        elif user == "help":
            print("Nova: Try hello, time, date, or bye.")

        else:
            print("Nova: Sorry, I don't understand that yet.")

chat()
