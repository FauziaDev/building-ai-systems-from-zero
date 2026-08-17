import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()
# Get API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found!")
# Create Groq client
client = Groq(api_key=api_key)
# Model
model = "llama-3.3-70b-versatile"
# Role
role = "user"
# 3 prompts
prompt1 = "Hi!"
prompt2 = """
Explain time travel in detail but under 100 words.
"""
prompt3 = """
Write a 1000 word essay on Machine Learning.
"""
# Store all prompts in a list
prompts = [prompt1, prompt2, prompt3]
# Run each prompt
for prompt in prompts:
    # Create message
    message = {
        "role": role,
        "content": prompt
    }
    # Messages list
    messages = [message]
    # Call Groq API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=5000
    )
    # Get AI response
    answer = response.choices[0].message.content
    # Get token usage
    usage = response.usage
    # Print everything
    print("=" * 60)
    print("PROMPT:")
    print(prompt)
    print("\nAI RESPONSE:")
    print(answer)
    print("\nTOKEN USAGE:")
    print("Prompt Tokens:", usage.prompt_tokens)
    print("Completion Tokens:", usage.completion_tokens)
    print("Total Tokens:", usage.total_tokens)
    print("\nFINISH REASON:")
    print(response.choices[0].finish_reason)
    print("=" * 60)