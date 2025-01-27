"""
Example 3: Crafting Few-Shot Prompt Templates
"""
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
]

example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="Question: {question}\nAnswer: {answer}"
)

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

print(prompt.format(input="What is the capital of Australia?"))
