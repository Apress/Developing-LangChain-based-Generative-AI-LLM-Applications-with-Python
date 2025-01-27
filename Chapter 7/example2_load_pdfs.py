"""
Example 2: Working with PDFs
"""
from langchain_community.document_loaders import PyPDFLoader

# Load the PDF file
loader = PyPDFLoader("media/2022 Annual Report ACME.pdf")

# Split and load pages
pages = loader.load_and_split()

# Print details about the document
print(f"Number of pages: {len(pages)}")
print(f"Content of the first page: {pages[0].page_content}")
print(f"Metadata of the 11th page: {pages[10].metadata}")
print(f"Characters in the first page: {len(pages[0].page_content)}")
