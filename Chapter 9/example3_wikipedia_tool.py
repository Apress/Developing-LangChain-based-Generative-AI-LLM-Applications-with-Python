"""
Example 3: Using the WikipediaQueryRun Tool
"""

!pip install langchain==0.2.5 langchain_openai==0.2.5 wikipedia

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Initialize the tool with custom configurations
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Try the tool
print("Tool Name:", tool.name)
print("Description:", tool.description)

# Search for "LangChain"
result = tool.run("LangChain")
print("Result:", result)
