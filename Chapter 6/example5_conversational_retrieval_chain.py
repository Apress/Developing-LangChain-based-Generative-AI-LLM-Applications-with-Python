"""
Example 5: Conversational Retrieval Chain
"""
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import ContextualCompressionRetriever
import os

# Initialize API key
openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Initialize retriever and LLM
retriever = ContextualCompressionRetriever(
    retriever=None,  # Replace with your configured retriever
    compressor=None  # Replace with your configured compressor
)
llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

# Create the Conversational Retrieval Chain
qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)

# Conversation loop
chat_history = []
print("Start a conversation with the assistant. Type 'exit' to quit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    result = qa_chain({"question": user_input, "chat_history": chat_history})
    chat_history.append((user_input, result['answer']))
    print(f"Assistant: {result['answer']}")
