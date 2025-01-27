"""
Example 5: Structured Chat Agent
"""

from langchain import hub
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

# Initialize tools
tools = [TavilySearchResults(max_results=1)]

# Define the prompt
prompt = hub.pull("hwchase17/structured-chat-agent")
prompt.messages[0].prompt.template = "You are a business analyst assistant."

# Initialize the agent
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
agent = create_structured_chat_agent(llm, tools, prompt)

# Run the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke({"input": "What are the best ways to reduce operational costs?"})

print(response)
