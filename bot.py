import datetime
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't eggs tell each other secrets? Because they might crack up.",
    "What did one wall say to the other? 'I'll meet you at the corner.'"
]

user_name = ""

def chatbot(userinput):
    global user_name
    userinput = userinput.lower().strip()

    if any(greet in userinput for greet in ["hello", "hi", "hey", "what's up"]):
        return f"Hey {user_name or 'there'}! How can I help you today?"

    elif "my name is" in userinput:
        user_name = userinput.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {user_name}!"

    elif "how are you" in userinput:
        return "I'm doing great thanks for asking! How are you feeling?"

    elif "i'm good" in userinput or "i am good" in userinput:
        return "Awesome!"

    elif "i'm sad" in userinput or "i am sad" in userinput:
        return "That's okay, bad days happen. Let's turn it around together"

    elif "okay" in userinput or "nice" in userinput:
        return "yeah!"

    elif "joke" in userinput:
        return random.choice(jokes)

    elif "your name" in userinput or "who are you" in userinput:
        return "I'm Bolt, your friendly rule-based chatbot! and what about you?"

    elif "time" in userinput:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    elif "date" in userinput:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."

    elif "day" in userinput:
        today = datetime.date.today()
        return f"Today is {today.strftime('%A')}."

    elif "help" in userinput or "commands" in userinput:
        return (
            "Here's what I can help with:\n"
            "Say 'hello' or 'hi'\n"
            "Introduce yourself\n"
            "Ask how I am, or tell me how you're feeling\n"
            "Ask for a joke\n"
            "Get the current time, date, or day\n"
            "Say 'bye' to exit"
        )

    elif any(bye in userinput for bye in ["bye", "goodbye", "see ya"]):
        return f"Catch you later, {user_name or 'friend'}!"

    else:
        return "Oops, I didn't get that. Try saying 'help' if you're stuck!"

# Start the chat
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("Chatbot:", response)

    if any(word in user_input.lower() for word in ["bye", "goodbye", "see ya"]):
        break