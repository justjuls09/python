"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[✓] 1. Header Docstring included.
[✓] 2. RESPONSES is a tuple containing at least 8 string options.
[✓] 3. Program uses a 'while True' loop to keep the game running.
[✓] 4. random.choice() selects the answer from the tuple.
[✓] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
Name: Julie Gavas
-----------------------------------------------------------------------
"""

import random

# --- MAGIC 8 BALL RESPONSES ---
RESPONSES = (
    "Yes!",
    "No!",
    "Maybe...",
    "Ask again later.",
    "Absolutely!",
    "Better not tell you now.",
    "The future is unclear.",
    "Definitely not.",
    "Signs point to yes.",
)

print("Welcome to the Digital Oracle!")
print("Ask any question, or type 'quit' to exit.\n")

# --- MAIN GAME LOOP ---
while True:
    # Ask the user a question
    question = input("What is your question? ")

    # Sanitize the input
    clean_question = question.strip().lower()

    # Exit condition
    if "quit" in clean_question:
        print("Goodbye! Error 404: User no longer found")
        break

    # Oracle's answer
    answer = random.choice(RESPONSES)

    # Display the answer
    print("Magic 8 Ball says:", answer, "\n")
