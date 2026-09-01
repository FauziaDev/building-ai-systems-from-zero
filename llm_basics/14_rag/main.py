import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found!")
client = Groq(api_key=api_key)
model = "llama-3.3-70b-versatile"
# Load knowledge from data.txt
with open("data.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()
question = "What is Fauzia learning?"
# RAG prompt
prompt = f"""
Answer the question using ONLY the information provided below.
Knowledge:
{knowledge}
Question:
{question}
Answer:
"""
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You answer questions using the provided knowledge."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)
print("Question:", question)
print("\nAI:", response.choices[0].message.content)