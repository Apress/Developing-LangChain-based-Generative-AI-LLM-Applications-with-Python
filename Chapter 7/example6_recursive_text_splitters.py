"""
Example 6: Recursive Character Text Splitters
"""
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

text = "This is a sample text. It consists of multiple sentences. Some sentences are longer than others. We will split this text into chunks."

# Using CharacterTextSplitter
char_splitter = CharacterTextSplitter(separator=". ", chunk_size=30, chunk_overlap=5)
char_chunks = char_splitter.create_documents([text])

print("CharacterTextSplitter:")
for chunk in char_chunks:
    print(chunk.page_content)
    print("---")

# Using RecursiveCharacterTextSplitter
recursive_splitter = RecursiveCharacterTextSplitter(separators=[". ", "! ", "? "], chunk_size=30, chunk_overlap=5)
recursive_chunks = recursive_splitter.create_documents([text])

print("RecursiveCharacterTextSplitter:")
for chunk in recursive_chunks:
    print(chunk.page_content)
    print("---")
