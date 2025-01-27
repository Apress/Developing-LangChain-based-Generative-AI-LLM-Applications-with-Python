"""
Example 10: Error Handling in Chains
"""
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Define prompt and chain
prompt = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
)
chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=prompt)

# Try-except block for error handling
try:
    result = chain.run("United States")
    print(result)
except Exception as e:
    print(f"An error occurred: {str(e)}")
