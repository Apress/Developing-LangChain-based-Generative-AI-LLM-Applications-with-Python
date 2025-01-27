"""
Example 7: LLaMA Text Generation with Hugging Face Pipeline
"""
import torch
from langchain import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, StoppingCriteria, StoppingCriteriaList
from huggingface_hub import login

# Authenticate with Hugging Face
login(token="Your access token")

# Load model and tokenizer
model_id = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Custom stopping criteria
class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids, scores, **kwargs):
        return tokenizer.eos_token_id in input_ids[0][-1]

# Create pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    stopping_criteria=StoppingCriteriaList([StopOnTokens()])
)

# Wrap pipeline in LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Generate response
prompt = "What are the potential benefits and risks of artificial intelligence?"
output = llm(prompt)
print(output)
