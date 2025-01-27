"""
Example 7: Testing Prompt Templates with and without Example Selector
"""
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.llms import OpenAI
import os

# Initialize API key
openai_api_key = os.environ.get("OPENAI_API_KEY", "your_openai_api_key_here")

# Few-shot examples
examples = [
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the currency of Japan?", "answer": "Japanese yen"},
]

# Example prompt template
example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="Question: {question}\nAnswer: {answer}"
)

# Without selector
prompt_without_selector = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

# With Length-Based Selector
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50
)

prompt_with_selector = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

# Load an LLM
llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, temperature=0.7)

# Test prompts
print("Prompt Template without Example Selector:")
print(prompt_without_selector.format(input="What is the capital of Australia?"))

print("\nGenerated Answer:")
print(llm(prompt_without_selector.format(input="What is the capital of Australia?")))

print("\nPrompt Template with Example Selector:")
print(prompt_with_selector.format(input="Who sculpted the Statue of David?"))

print("\nGenerated Answer:")
print(llm(prompt_with_selector.format(input="Who sculpted the Statue of David?")))
