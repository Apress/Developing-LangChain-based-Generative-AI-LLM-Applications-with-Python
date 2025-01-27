"""
Example 6: Loading LLaMA Tokenizer and Model with Hugging Face
"""
from transformers import LlamaTokenizer, LlamaForCausalLM

# LLaMA model and access token
model_name = "MetaAI/llama-7b"
access_token = "your_access_token"

# Load tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained(model_name, use_auth_token=access_token)
model = LlamaForCausalLM.from_pretrained(model_name, use_auth_token=access_token)

print("LLaMA model and tokenizer loaded successfully.")
