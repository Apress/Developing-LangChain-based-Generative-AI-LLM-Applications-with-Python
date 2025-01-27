"""
Example 4: Working with JSON Files
"""
from langchain_community.document_loaders import JSONLoader

# Load JSON data using a schema
loader = JSONLoader(
    file_path="./sample_data/products.json",
    jq_schema=".messages[].content",
    text_content=False
)
data = loader.load()

# Print loaded data
for item in data:
    print(f"Content: {item.page_content}\n")
    print(f"Metadata: {item.metadata}\n")
    print("---")

# Working with JSON Lines
jsonl_loader = JSONLoader(
    file_path="./sample_data/products.jsonl",
    jq_schema=".content",
    text_content=False,
    json_lines=True
)
jsonl_data = jsonl_loader.load()
print(jsonl_data)
