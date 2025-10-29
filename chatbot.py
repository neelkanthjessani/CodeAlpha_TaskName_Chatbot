# Basic Rule-Based Chatbot
# Run: python chatbot.py
# Type 'bye' to exit.

responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! What would you like to ask?",
    "how are you": "I'm fine, thanks! How about you?",
    "what is your name": "I am CodeAlpha Assistant Bot.",
    "bye": "Goodbye! Have a great day!"
}

def normalize(text):
    return text.lower().strip().rstrip("?.!")

def chatbot():
    print("=== Simple Chatbot ===")
    print("You can say: hello, how are you, what is your name, bye (to exit).")
    while True:
        user = input("You: ")
        key = normalize(user)
        if key == "bye":
            print("Bot:", responses.get("bye"))
            break
        reply = responses.get(key)
        if reply:
            print("Bot:", reply)
        else:
            print("Bot: Sorry, I don't understand. Try: hello / how are you / what is your name / bye.")

if __name__ == "__main__":
    chatbot()
