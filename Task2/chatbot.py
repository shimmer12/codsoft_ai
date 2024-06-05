import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': ['hello', 'hi', 'hey', 'greetings'],
            'about_products': ['tell me about your products', 'what do you sell', 'products'],
            'technical_support': ['help with technical issues', 'technical support', 'fix a problem'],
            'returns_policy': ['return policy', 'how to return a product', 'refund'],
            'farewell': ['bye', 'goodbye', 'see you later', 'exit']
        }
    
    def get_intent(self, user_input):
        for intent, patterns in self.responses.items():
            for pattern in patterns:
                if pattern in user_input:
                    return intent
        return 'general_query'
    
    def respond(self, intent):
        responses = {
            'greeting': "Hi there! How can I assist you today?",
            'about_products': "We offer a wide range of products. What specifically are you interested in?",
            'technical_support': "I’m here to help with any technical issues. Can you describe the problem?",
            'returns_policy': "You can return products within 30 days. Do you need help with a return?",
            'farewell': "Take care! Feel free to reach out if you have more questions.",
            'general_query': "I’m not sure I understand. Could you please provide more details?"
        }
        return responses.get(intent, "I'm not sure how to respond. Can you please provide more information?")
    
    def chat(self):
        print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")

        while True:
            user_input = input("You: ").lower()

            if user_input == 'exit':
                print("Chatbot: Goodbye! Have a great day.")
                break

            intent = self.get_intent(user_input)
            response = self.respond(intent)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
