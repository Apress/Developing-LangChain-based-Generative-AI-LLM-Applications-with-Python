# Chapter 2: Integrating LLM APIs with LangChain
# ----------------------------------------------

# Exercise 2: Using LangChain for Enhanced Flexibility

# Install the LangChain library using the following command:
# !pip install langchain

# Import the necessary modules
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LangChain with OpenAI's GPT
llm = OpenAI(api_key=api_key)

# Use LLMChain for easy interaction
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="You are a helpful chatbot. User: {user_input} Response:"
)

# Create an instance of LLMChain with the template
chain = LLMChain(llm=llm, prompt=prompt_template)

# Prompt the user for a story starter
user_prompt = input("Enter another story prompt: ")

# Call the run method on the LLMChain instance
response = chain.run(user_prompt)

# Print the generated response
print("Generated LangChain Response:", response)



