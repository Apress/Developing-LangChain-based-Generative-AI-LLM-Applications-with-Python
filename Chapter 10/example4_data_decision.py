"""
Example 4: Real-Time Data Decision-Making
"""

from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
import random

# Tools
def data_retrieval_tool():
    temperature = random.randint(20, 30)
    humidity = random.randint(40, 60)
    return f"Temperature: {temperature}°C, Humidity: {humidity}%"

def data_analysis_tool(data: str):
    if "Temperature: " in data:
        return "Data analyzed: Adjustments recommended for high humidity."
    return "Data analyzed: Conditions normal."

tools = [
    Tool(name="Data Retrieval", func=data_retrieval_tool, description="Retrieve real-time data."),
    Tool(name="Data Analysis", func=data_analysis_tool, description="Analyze data.")
]

# Initialize the agent
agent = initialize_agent(tools, OpenAI(temperature=0.7), agent="zero-shot-react-description", verbose=True)

# Test the agent
response = agent.run("Retrieve and analyze the current environmental conditions.")
print(response)
