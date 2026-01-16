def chatbot_response(user_input):
    user_input = user_input.lower()  

    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

def run_chatbot():
    print("Welcome to the Chatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

run_chatbot()
