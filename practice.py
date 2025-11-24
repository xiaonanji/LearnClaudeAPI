"""practice.py — small example script

Includes:
- greet(name): returns a greeting string
- add(a, b): returns the sum of two numbers

Run with: `python practice.py`
"""

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

def add_user_message(messages: list, content: str) -> None:
    user_message = {
        "role": "user",
        "content": content
    }
    messages.append(user_message)

def add_assistant_message(messages: list, content: str) -> None:
    assistant_message = {
        "role": "assistant",
        "content": content
    }
    messages.append(assistant_message)

def chat(messages: list, client: Anthropic, stop_sequences=[]) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-0",
        max_tokens=1000,
        messages=messages,
        stop_sequences=stop_sequences
    )
    return response.content[0].text

def main() -> None:
    client = Anthropic()

    messages = []
    add_user_message(messages, "Generate three different sample AWS CLI commands. Each should be very short")
    add_assistant_message(messages, "Here are the 3 commands without any comments:\n```bash")  

    text = chat(messages, client=client, stop_sequences=["```"])

    print(text)


if __name__ == "__main__":
    main()
