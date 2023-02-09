import eliza

chatbot = eliza.eliza()

print("Eliza: Hi, I am a therapist. How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "quit":
        break
    response = chatbot.respond(user_input)
    print("Eliza: " + response)

print("Eliza: Good bye! Take care.")
