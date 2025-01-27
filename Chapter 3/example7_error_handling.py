"""
Example 7: Error Handling
"""
from langchain_openai import ChatOpenAI
from openai.error import APIError, AuthenticationError, RateLimitError
from openai import OpenAI
import os

# Initialize OpenAI Client
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
client = OpenAI()
llm = ChatOpenAI()

try:
    # Example operation
    response = llm.invoke("Hello, how are you?")
    print("Response:", response)
except AuthenticationError as e:
    print(f"Authentication Error: {e}")
except RateLimitError as e:
    print("Rate limit exceeded. Try again later.")
except APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Operation completed.")
