import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

# Create Groq Client
client = Groq(api_key=api_key)

# Model Name
model = "llama-3.3-70b-versatile"

# Messages
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    # {
    #     "role": "user",
    #     "content": "Write one paragraph about Artificial Intelligence."
    # }
    {
        "role": "user",
        "content": "Write a motivational quote."
    }
]

# Generate Response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    # temperature=0
    # temperature = 0.5
    temperature = 1
)

# Print Answer
print(response.choices[0].message.content)