"""
Example 2: Using LangSmith to Evaluate Your Application
"""
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.smith import RunEvalConfig, run_on_dataset

import os

# Set API Keys
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["LANGCHAIN_API_KEY"] = "your_langsmith_api_key"

# Initialize the LLM and prompt
llm = ChatOpenAI(temperature=0)
prompt = PromptTemplate.from_template("Tell me a short joke about {topic}")
chain = LLMChain(llm=llm, prompt=prompt)

# Evaluation configuration
eval_config = RunEvalConfig(
    evaluators=["criteria", "embedding_distance"],
    custom_evaluators=[],
)

# Example dataset evaluation (ensure dataset_name exists in LangSmith)
# results = run_on_dataset(client=client, dataset_name="my-dataset", llm_or_chain_factory=chain, evaluation=eval_config)
# print(results)
