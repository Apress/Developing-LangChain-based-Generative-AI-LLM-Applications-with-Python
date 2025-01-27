"""
Example 2: Customer Support Automation
"""

from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

# Define a simple knowledge base search tool
def search_knowledge_base(query: str) -> str:
    if "password reset" in query.lower():
        return "To reset your password, follow these steps: ..."
    return "No specific answer found. Contact support for assistance."

tools = [Tool(name="Knowledge Base Search", func=search_knowledge_base, description="Search knowledge base.")]
memory = ConversationBufferMemory(memory_key="chat_history")

# Initialize the agent
agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent="conversational-react-description",
    verbose=True,
    memory=memory
)

# Test the agent
customer_query = "How do I reset my account password?"
response = agent.run(customer_query)
print(response)
