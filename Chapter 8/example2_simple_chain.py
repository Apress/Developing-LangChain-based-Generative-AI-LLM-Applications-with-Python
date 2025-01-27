"""
Example 2: A Simple Chain
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["product"],
    template="What are the benefits of {product}?",
)

# Initialize the LLM
llm = OpenAI(temperature=0.9)

# Create the Chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run the Chain
product_name = "Customer Service Chatbot"
response = chain.run(product_name)

print("Chain Response:")
print(response)
