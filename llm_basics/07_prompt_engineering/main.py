import os
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
        "content": "You are a helpful AI teacher."
    },
  {
#     "role": "user",
#    "content": "Classify this sentence as Positive or Negative: I love this phone."
# Rules:
# - Maximum 50 words.
# - Use very simple English.
# - Give exactly 2 examples.
# - No headings.
# """
  "role": "user",
#         "content": """
# Example:

# Sentence: I hate this movie.
# Answer: Negative

# Now classify this sentence:

# Sentence: I love this phone.
# Answer:
# """
"content": """
Example 1:
Sentence: I love this movie.
Answer: Positive

Example 2:
Sentence: This food is terrible.
Answer: Negative

Example 3:
Sentence: The weather is amazing.
Answer: Positive

Now classify:

Sentence: This phone is very bad.
Answer:
"""
}
]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.5
)
print(response.choices[0].message.content)