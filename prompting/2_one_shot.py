from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI()

sys_prompt = """
you are expert in writing and explaining the concepts ...

Input : what is EC2 in ASD STE100 formate?

Output : Amazon EC2 (Elastic Compute Cloud) is an AWS service that provides virtual computers over the internet.
            - Use: Run applications, websites, and LLMs.
            - Resources: CPU, RAM, storage, and optional GPU.
            - Cost: Pay for the resources you use.
            Example: You can use EC2 to host your own LLM in the cloud.
"""

result = client.responses.create(
    model = "openai.gpt-oss-120b",
    instructions = sys_prompt,
    input = [
        {
            "role" : "user",
            "content" : "what is RAG?"
        }
    ]
)

print(result.output_text)