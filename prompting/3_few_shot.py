from dotenv import load_dotenv
import os
load_dotenv()
from openai import OpenAI

client = OpenAI()

sys_prompt = """
you are expert in writing in ASD STE100 formate and explaining the concepts and to be precise to the point 

Input : what is EC2?
Output : Amazon EC2 (Elastic Compute Cloud) is an AWS service that provides virtual computers over the internet.
            - Use: Run applications, websites, and LLMs.
            - Resources: CPU, RAM, storage, and optional GPU.
            - Cost: Pay for the resources you use.
            Example: You can use EC2 to host your own LLM in the cloud.

Input : What is rocket science?
Output : Rocket Science
        Definition: Rocket science is the study of how rockets work and move through the air and space.
        Purpose:
            - To send satellites into space.
            - To transport astronauts into space.
            - To explore planets and other objects in space.

        Main Concepts:
            - Thrust: The force that moves a rocket forward.
            - Gravity: The force that pulls objects toward a planet.
            - Propulsion: The process that produces force to move a rocket.

        Example: A rocket uses thrust to move away from Earth and carry a satellite into space.
"""

result = client.responses.create(
    model = "openai.gpt-oss-120b",
    instructions = sys_prompt,
    input = [
        {
            "role" : "user",
            "content" : "what is wheel rotation?"
        }
    ]
)

print(result.output_text)