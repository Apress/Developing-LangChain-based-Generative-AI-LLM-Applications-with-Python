"""
Example 8: Router Chain
"""
from langchain.chains import LLMChain, RouterChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Chain 1: Sales queries
sales_prompt = PromptTemplate(
    template="Respond to the following sales query: {query}",
    input_variables=["query"]
)
sales_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=sales_prompt)

# Chain 2: Support queries
support_prompt = PromptTemplate(
    template="Respond to the following support query: {query}",
    input_variables=["query"]
)
support_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=support_prompt)

# Router Chain
router_chain = RouterChain.from_routes(
    routes=[
        ("sales", sales_chain),
        ("support", support_chain),
    ],
    default_chain=sales_chain,
    input_key="query",
    output_key="response"
)

# Run Router Chain
query = "I have a question about my order."
result = router_chain.run(query)
print(result)
