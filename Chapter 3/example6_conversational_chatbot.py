"""
Example 6: Conversational Chatbot
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

# Set the API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Initialize the chatbot model
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Chat function
def generate_response(text):
    messages = [HumanMessage(content=text)]
    response = chat_model.invoke(messages)
    return response.content

# Chat loop
while True:
    user_input = input("Enter a message (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    print("AI:", generate_response(user_input))
