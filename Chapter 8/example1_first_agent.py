"""
Example 1: Your First Agent
"""

from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Set up API keys (replace with your actual keys)
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["SERPAPI_API_KEY"] = "your_serpapi_api_key"

# Load the necessary tools
tools = load_tools(["serpapi", "llm-math"], llm=OpenAI(temperature=0))

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Generate an engaging article about {topic}."
)

# Initialize the agent
agent = initialize_agent(tools, OpenAI(temperature=0), agent="zero-shot-react-description", verbose=True)

# Run the agent with a user prompt
user_prompt = "What is the revenue increase due to the benefits of AI"
response = agent.run(prompt_template.format(topic=user_prompt))

print("Agent Response:")
print(response)
