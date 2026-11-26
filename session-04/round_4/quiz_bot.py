"""Quiz bot: ask the practice API five questions and print the answers.

Run it from the top folder of the repository:
    python session-04/round_4/quiz_bot.py
"""

from practice_api import ask
from time import sleep

QUESTIONS = [
    "What is a token?",
    "What is a context window?",
    "What does temperature change?",
    "What is a system prompt?",
    "What is a stack trace?",
]

for question in QUESTIONS:
    print(f"\nQ: {question}")
    try:
        answer = ask(question)
        print(f"A: {answer}")
        sleep(2)
    except Exception as e:
        print(f"Something went wrong: {e}")
