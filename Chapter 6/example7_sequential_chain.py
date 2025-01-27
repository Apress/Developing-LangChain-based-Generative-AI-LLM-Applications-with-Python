"""
Example 7: Sequential Chain
"""
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Chain 1: Generate keywords from a topic
topic_prompt = PromptTemplate(
    template="Generate relevant keywords for the topic: {topic}",
    input_variables=["topic"]
)
topic_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=topic_prompt)

# Chain 2: Fetch data based on keywords
data_prompt = PromptTemplate(
    template="Fetch data related to the following keywords: {keywords}",
    input_variables=["keywords"]
)
data_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=data_prompt)

# Chain 3: Summarize fetched data
summary_prompt = PromptTemplate(
    template="Summarize the following data: {data}",
    input_variables=["data"]
)
summary_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=summary_prompt)

# Create Sequential Chain
sequential_chain = SequentialChain(
    chains=[topic_chain, data_chain, summary_chain],
    input_variables=["topic"],
    output_variables=["summary"]
)

# Run Sequential Chain
topic = "Artificial Intelligence"
result = sequential_chain({"topic": topic})
print(result["summary"])
