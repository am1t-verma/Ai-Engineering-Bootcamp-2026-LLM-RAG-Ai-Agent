from dotenv import load_dotenv
load_dotenv()
import os
import time
from openai import OpenAI
from datetime import datetime

client = OpenAI()

messages = [
    {
        "role" : "system",
        "content" : """
You are a reliable, organized Daily TODO and Task Manager.

Rules:
1. Use the supplied current date and time when needed.
2. Format dates as: Friday, 2 October 2026, 1:30 PM.
3. Add tasks when requested.
4. Mark tasks completed only when explicitly instructed.
5. Never remove completed tasks unless deletion is explicitly requested.
6. Use [x] for completed tasks and [ ] for pending tasks.
7. Strike through completed task descriptions using ~~task~~.
8. Display completed tasks first, followed by pending tasks.
9. Preserve existing tasks and their statuses across the conversation.
10. Never invent tasks, deadlines, or completion statuses.
11. If the user asks for the full task list and no tasks exist, return exactly None.
12. If the user asks for pending tasks and none exist, return exactly None.
13. If a task command is ambiguous, ask one concise clarification question.
14. Be concise and follow the requested output format.
"""
    }
]
# print(messages)

def add_user_message(text : str):
    messages.append({
        "role" : "user",
        "content" : text
    })


def add_assistent_messages(text : str):
    messages.append(
        {
            "role" : "assistant",
            "content" : text
        }
    )

def chat(user_messages : str):
    current_time = datetime.now().strftime(
        "%A, %d %B %Y, %I:%M %p"
    )

    prompt = (
        f"Current date and time: {current_time}\n"
        f"User request: {user_messages}"
    )
    add_user_message(prompt)
    # print(f"after user messages : \n{messages}")

    result = client.responses.create(
        model = "openai.gpt-oss-120b",
        input = messages
    )
    output = result.output_text
    add_assistent_messages(output)
    return output

while True:
    message = input("\nWhat can I help you with? (type 'exit' to quit)\n> ").strip()

    if message.lower() == "exit":
        print("TODO manager closed.")
        break

    if not message:
        continue

    print(chat(message))