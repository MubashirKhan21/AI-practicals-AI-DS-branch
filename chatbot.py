import random

def greet():
    responses = ["Hi there! How can I assist you today?", "Hello! What can I do for you?", "Hey! How can I help you?"]
    return random.choice(responses)

def get_user_input():
    user_input = input("You: ")
    return user_input

def chatbot_response(user_input):
    greetings = ["hello", "hi", "hey"]
    goodbyes = ["bye", "goodbye", "see you"]
    
    if user_input.lower() in greetings:
        return greet()
    elif user_input.lower() in goodbyes:
        return "Goodbye! Have a great day!"
    else:
        return "I'm just a basic chatbot. I didn't understand that."

def main():
    print("Chatbot: " + greet())

    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    main()