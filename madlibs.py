"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[x] 1. Header Docstring included. File Name: madlibs.py
[x] 2. Program asks for at least 5 different inputs (variables).
[x] 3. Output uses F-Strings to combine text and variables.
[x] 4. Output uses at least one escape sequence (\n or \t).
[x] 5. Code contains comments explaining the steps.
[x] 6. Program runs without errors.
-----------------------------------------------------------------------
"""


# Get information from the user
player_name = input("Enter your name: ")
intelligence = input("Enter an intelligence level: ")
tool = input("Enter a type of tool: ")
action = input("Enter what action was used to win: ")
opponent = input("Enter the name of an opponent: ")
reward = input("Enter a type of reward: ")

# Create a story using f-strings
story = f"""

\t"Once upon a time, a player named {player_name} entered the School of Hard Knocks.
{player_name} had a skill level of {intelligence}, felt ready for anything.\n

That confidence was tested when a fierce opponent, {opponent}, appeared from the shadows. 
Both stood still for a moment, sizing each other up.\n

Armed only with {tool}, {player_name} took a deep breath and charged forward. 
The battle was intense, with both {player_name} and {opponent} analyzing and studying the enormous puzzle in front of them.\n 

With the crowd roaring, {player_name} focused all their energy and used {action} to outwit {opponent}.\n

As a reward, {player_name} received a {reward}, an honor reserved for someone that doesn't need coffee in the morning.\n

And from that day on, the tale of {player_name}’s triumph echoed throughout the school.

"""

#Print the story to the console
print(story)

#suggested inputs for testing:
# Name: Julie
# Intelligence level: Genius
# Tool: Magic Wand
# Action: Clever Strategy
# Opponent: Alex the Mighty
# Reward: Golden Trophy
