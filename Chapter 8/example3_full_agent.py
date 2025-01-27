"""
Example 3: Fully Working Agent
"""

# Install the required packages if not already installed
# !pip install langchain==0.0.153 openai==0.27.6 python-dotenv==1.0.0 google-search-results==2.4.2

import os
from dotenv import load_dotenv
import openai
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Load environment variables from the .env file
load_dotenv()

# Get the API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Confirm that the API keys are set correctly
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(model_name="gpt-4", temperature=0)

# Load the necessary tools
tools = load_tools(["serpapi", "llm-math"], llm=chat_model)

# Initialize the Agent
agent = initialize_agent(tools, chat_model, agent="zero-shot-react-description", verbose=True)

# Run the Agent with a query
query = (
    "A software company is planning to develop a new mobile app. They estimate that the initial development cost "
    "will be $200,000, and the app will generate a monthly revenue of $15,000. The company wants to know how many "
    "months it will take to break even on their investment, assuming a monthly maintenance cost of $5,000. Can you "
    "help calculate the breakeven point?"
)
response = agent.run(query)

print("Agent Response:")
print(response)
