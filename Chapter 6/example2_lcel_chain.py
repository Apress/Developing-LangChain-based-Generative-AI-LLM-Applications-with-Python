"""
Example 2: LCEL Chain
"""
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import load_chain
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Define the prompt template
template = "What is the capital of {country}?"
prompt = PromptTemplate(template=template, input_variables=["country"])

# Create and run the LCEL Chain
chain = load_chain("llm_chain", llm=OpenAI(openai_api_key=openai_api_key), prompt=prompt)
result = chain.run("France")
print(result)
