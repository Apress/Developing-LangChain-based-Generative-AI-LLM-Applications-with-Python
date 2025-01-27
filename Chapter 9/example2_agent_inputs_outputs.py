"""
Example 2: Using Agent Inputs and Outputs
"""

from langchain_core.agents import AgentAction, AgentFinish

# Define the agent input
agent_input = {
    "intermediate_steps": [
        (AgentAction(tool="Search", tool_input="What is the capital of France?", log="Searching for the capital of France"), 
         "Paris is the capital of France.")
    ]
}

# Simulated agent execution
def run_agent(input_data):
    # Simulate an agent's thought process
    return AgentFinish(return_values={"output": "The capital of France is Paris."})

agent_output = run_agent(agent_input)

if isinstance(agent_output, AgentAction):
    print("Agent wants to take the following action:", agent_output)
elif isinstance(agent_output, AgentFinish):
    print("Agent has finished with the following response:", agent_output.return_values)
