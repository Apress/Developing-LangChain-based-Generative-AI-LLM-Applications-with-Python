"""
Example 4: Using PydanticOutputParser for Movie Data
"""
from pydantic import BaseModel, Field, ValidationError, field_validator
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# Define the Movie Data Model
class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    director: str = Field(description="The director of the movie")
    year: int = Field(description="The release year of the movie")
    
    # Quality control: Ensure the movie title is capitalized
    @field_validator("title")
    def title_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Movie title must be capitalized.")
        return value

# Initialize the Output Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Create a Prompt Template
prompt = PromptTemplate(
    template="Please provide information about a movie in the following format:\n{format_instructions}\nQuestion: {query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Set up the OpenAI API key
openai_api_key = os.environ.get("OPENAI_API_KEY", "your_openai_api_key_here")

# Initialize the language model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)

# Query for the movie
query = "Tell me about the movie 'Inception'."
human_message = HumanMessage(content=prompt.format(query=query))
response = llm([human_message])

# Parse the response
try:
    parsed_movie = parser.parse(response.content)
    print(parsed_movie)
except ValidationError as e:
    print(f"Validation Error: {e}")
