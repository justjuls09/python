"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[x] 3. Program takes a word and uppercases it.
[x] 4. Program loops through letters and prints NATO words.
[x] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""
"""
Author: Julie Gavas
Program: data_mapper
Purpose: Allows us to map complex relationships
"""
NATO_ALPHABET = {
    "A": "Alpha",   "B": "Bravo",    "C": "Charlie",
    "D": "Delta",   "E": "Echo",     "F": "Foxtrot",
    "G": "Golf",    "H": "Hotel",    "I": "India",
    "J": "Juliett", "K": "Kilo",     "L": "Lima",
    "M": "Mike",    "N": "November", "O": "Oscar",
    "P": "Papa",    "Q": "Quebec",   "R": "Romeo",
    "S": "Sierra",  "T": "Tango",    "U": "Uniform",
    "V": "Victor",  "W": "Whiskey",  "X": "X-ray",
    "Y": "Yankee",  "Z": "Zulu"
}

# Get user input and convert to uppercase
word = input("Enter word to spell: ").upper().strip()

# Loop through each character

for char in word:
    try:
	# try to print the NATO code

        print(NATO_ALPHABET[char])
    except KeyError:

        # If character is missing

        print(f"'{char}' is not a valid letter in the NATO alphabet.")


