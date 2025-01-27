"""
Example 1: Basic LLMChain
"""
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Define the prompt template
template = "What is the capital of {country}?"
prompt = PromptTemplate(template=template, input_variables=["country"])

# Initialize the LLM
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)

# Create the LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run("France")
print(result)
