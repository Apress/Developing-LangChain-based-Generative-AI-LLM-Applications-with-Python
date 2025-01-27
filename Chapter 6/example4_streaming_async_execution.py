"""
Example 4: Streaming and Async Execution
"""
import asyncio
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Define the chain
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)
chain = LLMChain(llm=llm, prompt=prompt)

# Async function to generate names
async def generate_names(product):
    return await chain.arun({"product": product})

# Run async tasks
products = ["smartphone", "laptop", "smartwatch"]
results = asyncio.run(asyncio.gather(*(generate_names(product) for product in products)))
for product, name in zip(products, results):
    print(f"Product: {product}, Name: {name}")
