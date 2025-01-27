"""
Example 1: Loading Text Files
"""
from langchain_community.document_loaders import TextLoader

# Load a single text file
loader = TextLoader("media/file1.txt")

# Load the documents
documents = loader.load()

# Print the loaded documents
for doc in documents:
    print(f"Content: {doc.page_content}\n")
    print(f"Metadata: {doc.metadata}\n")
    print("---")
