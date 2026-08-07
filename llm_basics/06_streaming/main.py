import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

# Create Client
client = Groq(api_key=api_key)

# Streaming Request
stream = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "Explain Artificial Intelligence in simple words."
        }
    ],
    temperature=0.7,
    stream=True
)

print("AI: ", end="", flush=True)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()