"""
Example 6: Few-Shot Prompts with Example Selector
"""
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

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

# Initialize the selector
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50
)

# Create a FewShotPromptTemplate using the selector
prompt_with_selector = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

# Test the template with a selector
print("Prompt with Example Selector:")
print(prompt_with_selector.format(input="Who sculpted the Statue of David?"))
