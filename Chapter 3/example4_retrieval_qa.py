"""
Example 4: Retrieval-Based Question Answering
"""
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader

# Load and prepare data
loader = TextLoader("your_data.txt")
documents = loader.load()

# Create a vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)

# Initialize the language model
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# Create the retrieval chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Use the chain
query = "Your question here"
result = qa_chain.invoke({"query": query})
print("Q&A Response:", result['result'])
