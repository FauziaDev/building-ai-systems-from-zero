
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

print(my_api_key)

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Explain the importance of fast language models"
message={
    "role": role,
    "content": prompt
}
messages = [message]
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models"
        }
    ]
)

print(response.choices[0].message.content)
