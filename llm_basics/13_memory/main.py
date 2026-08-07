import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"


# Memory
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


print("🤖 AI with Memory")
print("Type 'exit' to quit.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # User message ko memory me add karo
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.5
    )

    answer = response.choices[0].message.content

    print("\nAI:", answer)

    # AI ka answer bhi memory me save karo
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    