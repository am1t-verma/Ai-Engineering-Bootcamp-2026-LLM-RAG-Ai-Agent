import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY"),
)

completion = client.chat.completions.create(
    model="z-ai/glm-5.3-flash",
    messages=[
        {"role": "user", "content": "Hello!"},
    ],
    temperature=0.5,
    max_tokens=1024,
)

print(completion.choices[0].message.content)