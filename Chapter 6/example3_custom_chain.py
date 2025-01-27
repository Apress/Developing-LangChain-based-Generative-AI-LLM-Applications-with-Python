"""
Example 3: Custom Chain
"""
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Initialize the LLM
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

# Create the custom chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run("smartphone")
print(result)
