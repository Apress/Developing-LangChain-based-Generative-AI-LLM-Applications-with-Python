"""
Example 1: Simple Chain for Generative AI
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Initialize the LLM model
llm = ChatOpenAI()

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical documentation writer."),
    ("user", "{input}")
])

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Use the chain
result = chain.run("Explain the concept of recursion in programming.")
print("Generated Response:", result)
