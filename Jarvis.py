import random

# Define a list of possible responses
responses = {"how are you": "I'm fine, thank you for asking.",
             "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!"}

# Define a function to respond to user input
def respond(user_input):
    # Check if the user input matches a specific question in the responses dictionary
    if user_input.lower() in responses:
        return responses[user_input.lower()]

    # If the user input is not a specific question, choose a random response from a list of greetings
    greetings = ["Hello, how can I assist you?", "Good day, what can I do for you?", "Hi, how can I help you today?"]
    return random.choice(greetings)

# Start the chatbot
print("Hi, I'm Jarvis, your personal assistant.")

# Loop through the conversation until the user ends it
while True:
    # Get user input
    user_input = input("You: ")

    # Respond to user input
    bot_response = respond(user_input)

    # Display the bot's response
    print("Jarvis:", bot_response)

    # Check if the user wants to end the conversation
    if user_input.lower() == "bye":
        print("Jarvis: Goodbye, have a nice day!")
        break
