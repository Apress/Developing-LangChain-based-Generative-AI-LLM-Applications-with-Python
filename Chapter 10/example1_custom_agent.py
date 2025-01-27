"""
Example 1: Creating a Custom Agent
"""

from langchain_openai import ChatOpenAI
from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor

# Load the language model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Define a simple tool
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

# Define tools
tools = [get_word_length]

# Create a prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a very powerful assistant."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Bind tools to the language model
llm_with_tools = llm.bind_tools(tools)

# Create the agent
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(x["intermediate_steps"]),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)

# Create the AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Test the agent
response = list(agent_executor.stream({"input": "How many letters are in the word 'LangChain'?"}))
print(response)
