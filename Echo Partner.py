import spacy
import random

# Load English tokenizer, POS tagger, etc.
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greet": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "thx", "appreciate it"],
    "weather": ["what's the weather", "weather like", "rain", "sunny", "forecast"],
    "name": ["what is your name", "who are you", "your name"]
}

responses = {
    "greet": ["Hello there!", "Hey! How can I help?", "Hi, I'm Echo!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help."],
    "weather": ["It's always sunny in the cloud ", "No rain here—just code!"],
    "name": ["I'm Echo, your AI conversational partner!", "They call me Echo, the chatbot."]
}

def predict_intent(text):
    doc = nlp(text.lower())
    for intent, keywords in intents.items():
        for token in doc:
            if token.text in keywords:
                return intent
    return "unknown"

def ai_echo_response(user_input):
    intent = predict_intent(user_input)
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return "Hmm, I didn't quite get that. Could you rephrase?"

# Chat loop
if __name__ == "__main__":
    print("AI Echo : Hello! I’m your smartest conversational partner. Ask me anything!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI Echo : Goodbye! ")
            break
        response = ai_echo_response(user_input)
        print(f"AI Echo : {response}")
