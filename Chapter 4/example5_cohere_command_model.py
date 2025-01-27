"""
Example 5: Creative Text with Cohere Command Model
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
import os

# Set up Cohere API key
os.environ["COHERE_API_KEY"] = "YOUR_COHERE_API_KEY"

# Prompt template
system_prompt = """
You are an AI assistant created to generate creative business pitches. Please continue the following pitch:
Pitch: Introducing a revolutionary new product that will transform the way people work and collaborate. Our innovative solution combines cutting-edge technology with intuitive design to create a seamless experience for teams of all sizes.
"""

# Initialize the Cohere model
cohere = ChatCohere(temperature=0, api_key=os.getenv("COHERE_API_KEY"), model_name="command-r")

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{text}")
])

# Create a chain and generate a response
chain = prompt | cohere
response = chain.invoke({"text": "Continue the pitch."})
print("Generated Pitch:", response)
