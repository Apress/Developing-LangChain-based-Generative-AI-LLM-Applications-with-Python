Chapter 2: Integrating LLM APIs with LangChain
This repository contains example scripts from Chapter 2 of the book, "Develop LangChain-Based Generative AI LLM Apps Using Python". These examples showcase how to integrate Large Language Model (LLM) APIs with LangChain, focusing on setting up your Python environment, securely configuring API keys, and leveraging LangChain for enhanced flexibility and reusability.

Examples
1. Calling an LLM API Directly
File: example1_calling_llm_api.py
Description: This script demonstrates how to call the OpenAI API directly using the Chat Completion API. You'll learn to configure the API key and send a simple prompt to generate responses.
2. Using LangChain for Enhanced Flexibility
File: example2_langchain_flexibility.py
Description: This example explores the seamless integration of LangChain with OpenAI. It highlights how LangChain simplifies the process of creating flexible and reusable pipelines for interacting with LLMs.

Setup Instructions
Prerequisites
Python 3.7 or later
An OpenAI API key

Steps to Run the Examples
Download and Save the Files

Clone this repository or download the files example1_calling_llm_api.py and example2_langchain_flexibility.py.

Set Up Your Environment:
Install the required libraries:

pip install openai==0.28 langchain

Configure your OpenAI API key as an environment variable:
macOS/Linux:
export OPENAI_API_KEY=your_api_key_here

Windows:
set OPENAI_API_KEY=your_api_key_here
Run the Scripts

Use your terminal or preferred IDE to execute the scripts

python example1_calling_llm_api.py

python example2_langchain_flexibility.py

Interact with the Prompts

Follow the instructions in the terminal. Provide inputs when prompted and observe the generated outputs.

Key Features Demonstrated
Direct API Interaction: Learn how to make basic requests to OpenAI’s API and handle responses.
LangChain Integration: Understand how LangChain enhances the flexibility of LLM interactions by abstracting boilerplate code and streamlining workflows.

About the Book
This repository is part of the book, "Generative AI Apps With LangChain and Python", which guides readers through building intelligent applications with LangChain, Pinecone, and OpenAI. For more information, visit https://www.amazon.com/Generative-Apps-LangChain-Python-Project-Based-ebook/dp/B0DLGM96L5/ref=tmm_kin_swatch_0