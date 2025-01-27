from openai import OpenAI
import os

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "Your OpenAI key"

client = OpenAI()

prompt = "Provide a brief market analysis for a new eco-friendly, reusable water bottle."

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a market research analyst with expertise in consumer goods."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150,
    n=1,
    temperature=0.6,
)

print("Market Analysis:", response.choices[0].message.content)
