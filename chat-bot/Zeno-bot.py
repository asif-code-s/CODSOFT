import re
import random
import datetime


jokes =['Why did the scarecrow win an award? Because he was outstanding in his field!',
         'Why don’t scientists trust atoms? Because they make up everything!',
         'Why did the bicycle fall over? Because it was two-tired!',
         'What do you call fake spaghetti? An impasta!',
         'Why did the math book look sad? Because it had too many problems!']


print("\nHello 👋, I am a Zeno, your friendly chat bot!, Type 'exit' to stop the chat.")

while True:
    
    a=input("\nYou: ").lower()
    
    if 'hello' in a or 'hi' in a:
        print("Zeno: Hello! How can I help you today?")
    elif'how are you?' in a:
        print("Zeno: I'm just a program, but thanks for asking! How can I assist you?")
    elif 'what is your name?' in a:
        print("Zeno: I am a simple chat bot created to assist you.")
    elif re.search(r'\bweather\b', a):
        print("Zeno: I don't have real-time weather data, but you can check a weather website for updates.")
    elif re.search(r'\btime\b', a):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Zeno: The current time is 🕒 {current_time}.")
    elif re.search(r'\bdate\b', a):
        current_date = datetime.datetime.now().strftime("%d-%m-%y")
        print(f"Zeno: The current date is 📅 {current_date}.")
    elif re.search(r'\b(what|who) (is|are) (your|my|you) (name|names)\b', a):
        print("Zeno: I am Zeno, your friendly chat bot. What about you?")
    elif re.search(r'\b(joke|comedy|fun)\b', a):
        print("Zeno: Here's a joke for you 🤣: " + random.choice(jokes))
    elif re.search(r'\bhelp\b', a):
        print("Zeno: Sure! What do you need help with?")
    elif re.search(r"\b(i feel|i am feeling|i'm|i am) (sad|lonely|depressed|low)\b", a):
        print("Zeno: I'm sorry to hear that you're feeling this way 💔. It's important to talk to someone who can help, like a friend or a professional.")
    elif re.search(r'\b(what|where|when|why)\b', a):
        print("Zeno: That's an interesting question! Can you provide more details?")
    
    
    elif a=='exit' :
        print("Zeno: Goodbye! Have a great day!")
        break
    
    else:
        print("Zeno: I'm not sure how to respond to that. Can you ask something else?")