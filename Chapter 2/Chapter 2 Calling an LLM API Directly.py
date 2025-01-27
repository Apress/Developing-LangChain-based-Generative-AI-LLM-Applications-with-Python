# Chapter 2: Integrating LLM APIs with LangChain

# Exercise 1: Calling an LLM API Directly

# Install the required library using the following command in your terminal or notebook:
# !pip install openai==0.28

import os
import openai

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = "your_api_key_here"

# Confirm that the API key is set correctly
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to get the chat completion
def get_chat_completion(user_prompt):
    """
    Generate a response using OpenAI's ChatCompletion API.
    """
    from openai import ChatCompletion
    response = ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.choices[0].message.content.strip()

# Prompt the user to enter a story prompt
user_prompt = input("Enter a story prompt: ")

# Generate the chat completion based on the user prompt
result = get_chat_completion(user_prompt)

# Print the generated result
print("Generated Response:", result)
