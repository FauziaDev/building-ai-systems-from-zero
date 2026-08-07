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


# Tools
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]


messages = [
    {
        "role": "user",
        "content": "First calculate 10 + 5, then multiply the result by 2."
    }
]


# Agent loop
while True:

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # AI final answer
    if not message.tool_calls:
        print("\nAI:", message.content)
        break

    # Add AI message to conversation
    messages.append(message)

    # Execute tools
    for tool_call in message.tool_calls:

        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("\nTool:", function_name)
        print("Arguments:", arguments)

        if function_name == "add":
            result = add(arguments["a"], arguments["b"])

        elif function_name == "multiply":
            result = multiply(arguments["a"], arguments["b"])

        print("Result:", result)

        # Send tool result back to AI
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )