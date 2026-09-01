import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, ValidationError

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

client = Groq(api_key=api_key)

model = "llama-3.1-8b-instant"


# Pydantic Model
class PythonInfo(BaseModel):
    name: str
    type: str
    difficulty: str


messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Return only valid JSON."
    },
    {
        "role": "user",
        "content": """
Give information about Python.

Return JSON in this exact format:

{
    "name": "Python",
    "type": "Programming Language",
    "difficulty": "Easy"
}
"""
# "content": """
# Return JSON in this format:

# {
#     "name": 123,
#     "type": "Programming Language",
#     "difficulty": true
# }
# """
    }
]


response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.2
)

answer = response.choices[0].message.content

print("AI Response:")
print(answer)

try:
    # Validate AI response
    python_info = PythonInfo.model_validate_json(answer)

    print("\n############################")
    print("Validation Successful ✅")
    print("Name:", python_info.name)
    print("Type:", python_info.type)
    print("Difficulty:", python_info.difficulty)

except ValidationError as e:
    print("\nValidation Failed ❌")
    print(e)