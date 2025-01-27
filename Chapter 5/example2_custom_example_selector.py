"""
Example 2: Creating a Custom Example Selector
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any

# Define the BaseExampleSelector class
class BaseExampleSelector(ABC):
    @abstractmethod
    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
        pass

    @abstractmethod
    def add_example(self, example: Dict[str, str]) -> Any:
        pass

# Define the CustomExampleSelector
class CustomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples

    def add_example(self, example):
        self.examples.append(example)

    def select_examples(self, input_variables):
        new_word = input_variables["input"]
        new_word_length = len(new_word)
        smallest_diff = float("inf")
        best_match = None

        for example in self.examples:
            current_diff = abs(len(example["input"]) - new_word_length)
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                best_match = example

        return [best_match]

# Usage
examples = [
    {"input": "hi", "output": "ciao"},
    {"input": "bye", "output": "arrivaderci"},
    {"input": "soccer", "output": "calcio"},
]

example_selector = CustomExampleSelector(examples)
print(example_selector.select_examples({"input": "okay"}))  # [{'input': 'bye', 'output': 'arrivaderci'}]

example_selector.add_example({"input": "hand", "output": "mano"})
print(example_selector.select_examples({"input": "okay"}))  # [{'input': 'hand', 'output': 'mano'}]
