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


# Python function
def add(a, b):
    return a + b


# Tool definition
tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    }
]


messages = [
    {
        "role": "user",
        "content": "What is 25 + 30?"
    }
]


response = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"
)


message = response.choices[0].message

print("AI Response:")
print(message)

if message.tool_calls:
    tool_call = message.tool_calls[0]

    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print("\nFunction:", function_name)
    print("Arguments:", arguments)

    if function_name == "add":
        result = add(arguments["a"], arguments["b"])

        print("Result:", result)