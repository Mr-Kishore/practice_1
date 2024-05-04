import datetime
import random

def greet():
    responses = ["hello", "Hi there", "Hey! How can i assist you today?"]
    return random.choice(responses)

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}"
    
def get_date():
    current_date = datetime.date.today().strftime("%A,%B,%d,%Y")
    return f"The current time is {current_date}."

def tell_advices():
    advice = [
        "Money makes a man", 
              "Life gets peaceful if you have enough money", 
              "Never beg for love"
              ]
    return random.choice(advice)

def assistant(command):
    if "time" in command:
        return get_time()
    elif "date" in command:
        return get_date()
    elif "advice" in command:
        return tell_advices()
    else:
        return "Sorry, I dont understand the command"
    
if __name__ == "__main__":
    print(greet())
    while True:
        user_input = input("How can I assist you?")
        if user_input.lower() == "exit":
            print("GOODBYE!")
            break
        else:
            print(assistant(user_input))