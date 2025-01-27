import os
import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

# Streamlit app UI setup
st.title("ChatGPT-like Q&A App")
st.subheader("Interact with an AI to answer your questions.")

# User query input
user_query = st.text_input("Enter your question:")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history
if st.session_state['chat_history']:
    st.markdown("### Chat History")
    for chat in st.session_state['chat_history']:
        st.write(f"**Q:** {chat['question']}")
        st.write(f"**A:** {chat['answer']}")
        st.write("---")

# Check for user input and handle submission
if user_query and st.button("Submit"):
    # Load the language model
    llm = ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo')

    # Define the prompt
    prompt = ChatPromptTemplate.from_messages([
        Human
