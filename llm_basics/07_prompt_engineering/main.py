import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# model = "llama-3.3-70b-versatile"
# model = "llama-3.1-8b-instant"
model = "openai/gpt-oss-20b"
# 1️⃣ ZERO-SHOT
messages = [
    {
        "role": "system",
        "content": "Classify the sentence as Positive or Negative."
    },
    {
        "role": "user",
        "content": "I love this phone."
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.5
)

print("ZERO-SHOT:")
print(response.choices[0].message.content)
# 2️⃣ ONE-SHOT
messages = [
    {
        "role": "system",
        "content": "Classify the sentence as Positive or Negative."
    },
    {
        "role": "user",
        "content": """
Example:
I hate this movie. → Negative

Now classify:
I love this phone. →
"""
    }
]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.5
)
print("\nONE-SHOT:")
print(response.choices[0].message.content)
# 3️⃣ FEW-SHOT
messages = [
    {
        "role": "system",
        "content": "Classify the sentence as Positive or Negative."
    },
    {
        "role": "user",
        "content": """
Example 1:
I love this movie. → Positive

Example 2:
This food is terrible. → Negative

Example 3:
The weather is amazing. → Positive

Now classify:
This phone is very bad. →
"""
    }
]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.5
)
print("\nFEW-SHOT:")
print(response.choices[0].message.content)