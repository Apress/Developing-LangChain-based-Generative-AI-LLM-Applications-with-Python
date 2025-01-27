"""
Example 9: Conditional Chain
"""
from langchain.chains import LLMChain, ConditionalChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Chain 1: Positive sentiment
positive_prompt = PromptTemplate(
    template="Respond positively to the following query: {query}",
    input_variables=["query"]
)
positive_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=positive_prompt)

# Chain 2: Negative sentiment
negative_prompt = PromptTemplate(
    template="Respond cautiously to the following query: {query}",
    input_variables=["query"]
)
negative_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=negative_prompt)

# Conditional Chain
sentiment_conditions = [
    ("positive", positive_chain),
    ("negative", negative_chain),
]
conditional_chain = ConditionalChain.from_conditions(
    conditions=sentiment_conditions,
    default_chain=positive_chain,
    input_key="query",
    output_key="response"
)

# Run Conditional Chain
query = "I love your product!"
result = conditional_chain.run(query)
print(result)
