"""
Example 4: Fun Facts with Anthropic Claude
"""
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
import os

# Set up Anthropic API key
os.environ["ANTHROPIC_API_KEY"] = "YOUR_ANTHROPIC_API_KEY"

# Define the system and human prompts
system_prompt = """
You are an AI assistant created by Anthropic to be helpful, harmless, and honest. 
Please provide a fun fact about AI.
"""

# Initialize the Anthropic model
claude = ChatAnthropic(temperature=0, api_key=os.getenv("ANTHROPIC_API_KEY"), model_name="claude-3-sonnet-20240229")

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{text}")
])

# Use the prompt to create a chain
chain = prompt | claude

# Generate a response
response = chain.invoke({"text": "Give me a fun fact about Claude"})
print("Fun Fact:", response)
