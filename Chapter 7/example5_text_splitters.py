"""
Example 5: Text Splitters
"""
from langchain_text_splitters import CharacterTextSplitter

# Load a text document
with open("./sample_data/The Art of Money Getting.txt") as f:
    document = f.read()

# Initialize a text splitter
text_splitter = CharacterTextSplitter(
    separator="\n\n", chunk_size=1000, chunk_overlap=200, length_function=len
)

# Create chunks of text
chunks = text_splitter.create_documents([document])

# Print one of the chunks
print(chunks[4])
