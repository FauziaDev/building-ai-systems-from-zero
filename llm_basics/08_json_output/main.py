import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Always return the answer as valid JSON."
    },
    {
        "role": "user",
        "content": """
Give information about Python.

Return only JSON in this format:

{
    "name": "Python",
    "type": "Programming Language",
    "difficulty": "Easy"
}
"""
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.2
)

answer = response.choices[0].message.content

print(answer)

data = json.loads(answer)

print("############################")
print("Name:", data["name"])
print("Type:", data["type"])
print("Difficulty:", data["difficulty"])