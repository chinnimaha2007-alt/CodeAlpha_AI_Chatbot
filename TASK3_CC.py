# AI Powered Chatbot
# Retrieval-Based Chatbot for Website Support
# Predefined questions and responses
responses = {
    "hello": "Hello! Welcome to our website. How can I help you?",
    "hi": "Hi there! How may I assist you today?",
    "services": "We provide cloud computing, web development, and AI solutions.",
    "pricing": "Our pricing depends on the selected service package.",
    "contact": "You can contact us at support@example.com.",
    "bye": "Thank you for visiting. Have a great day!"
}
# Function to generate chatbot response
def chatbot_response(user_input):
    # Convert input to lowercase for matching
    user_input = user_input.lower()
    # Check if input exists in predefined patterns
    if user_input in responses:
        return responses[user_input]
    # Default response
    return "Sorry, I couldn't understand that. Please try another question."
# Main chatbot loop
print("===== AI Powered Chatbot =====")
print("Type 'bye' to exit.\n")
while True:
    # Take user input
    user_message = input("You: ")
    # Generate response
    bot_reply = chatbot_response(user_message)
    # Display chatbot response
    print("Bot:", bot_reply)
    # Exit condition
    if user_message.lower() == "bye":
        break
print("\nChatbot Session Ended")