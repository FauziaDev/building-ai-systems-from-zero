import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

# Create client
client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

# Conversation History
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("🤖 AI Chatbot with Memory Started")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Save user message
    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Get AI response
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )

    answer = response.choices[0].message.content

    print("\nAI:", answer)
    print()

    # Save AI response
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )