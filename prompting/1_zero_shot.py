import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI()

result = client.responses.create(
    model="openai.gpt-oss-120b",
    input = [
        {
            "role" : "user",
            "content" : "what is LLM inference?"
        }
    ]
)

print(result.output_text)