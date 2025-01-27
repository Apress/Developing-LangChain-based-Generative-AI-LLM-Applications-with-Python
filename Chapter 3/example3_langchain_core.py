"""
Example 3: Using LangChain Core
"""
from langchain_core.language_models import BaseLLM
from langchain_openai import ChatOpenAI

# Initialize your language model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Use the model
response = llm.invoke("Tell me a joke about programming.")
print("LangChain Core Response:", response.content)
