"""
Example 1: Using a Prompt Template with an LLM
"""
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["algorithm", "language"],
    template="""You are a seasoned software engineer.
Explain the following algorithm: {algorithm} in {language}. 
Describe its purpose, time complexity, and a common use case."""
)

# Initialize the LLM
llm = OpenAI(openai_api_key="your_openai_key", temperature=0.7)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Generate a response
response = chain.run(algorithm="machine learning", language="French")
print(response)
