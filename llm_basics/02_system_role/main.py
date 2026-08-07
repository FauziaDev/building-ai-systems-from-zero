import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

# Create Groq client
client = Groq(api_key=api_key)

# Model name
model = "llama-3.3-70b-versatile"

# Messages
messages = [
    # {
    #     "role": "system",
    #     "content": "You are a helpful Python teacher. Explain everything in very simple English with examples."
    # },
    {
    "role": "system",
    # "content": "You are a Hindi teacher."
    "content": "You are a English teacher."
    },
    {
        "role": "user",
        "content": "What is a variable in Python?"
    }
]

# Generate response
response = client.chat.completions.create(
    model=model,
    messages=messages,
)

# Print response
print(response.choices[0].message.content)