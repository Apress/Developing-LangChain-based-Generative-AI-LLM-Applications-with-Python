"""
Example 5: Building a Chat Prompt Template
"""
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
import os

# Set up the OpenAI API key
openai_api_key = os.environ.get("OPENAI_API_KEY", "your_openai_api_key_here")

# Initialize the chat model
chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

# Define the chat template
template = """
You are an enthusiastic assistant that rewrites the user's text to sound more exciting.

User: {text}
Assistant:
"""

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are an enthusiastic assistant that rewrites the user's text to sound more exciting."
    ),
    HumanMessagePromptTemplate.from_template("{text}"),
])

# Get user input
user_input = input("Enter some text: ")

# Format the prompt
formatted_prompt = prompt.format_prompt(text=user_input)

# Print the formatted prompt
print("\nFormatted Prompt:")
print(formatted_prompt.to_messages())

# Generate the chat response
response = chat(formatted_prompt.to_messages())

# Print the assistant's response
print("\nAssistant's Response:")
print(response.content)
