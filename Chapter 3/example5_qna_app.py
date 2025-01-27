"""
Example 5: Building a Simple Q&A Application
"""
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Output Parser
output_parser = StrOutputParser()

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a wellness expert."),
    ("user", "{input}")
])

# Create the chain
llm = OpenAI(api_key="openai_api_key")
chain = prompt | llm | output_parser

# Test the chain
output = chain.invoke({"input": "What are the benefits of walking a mile a day?"})
print("Wellness Q&A:", output)
