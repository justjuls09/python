"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[✓] 1. Header Docstring included with your name.
[✓] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[✓] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[✓] 4. Task 3: Validation (isdigit check) completed.
[✓] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Julie Gavas
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR ---
instrument = "Acoustic Guitar"

# Print the length of 'instrument'
print("Length of instrument:", len(instrument))

# Print the first and last letter
print("First letter:", instrument[0])
print("Last letter:", instrument[-1])

# Print lowest and highest ASCII characters
print("Lowest ASCII character:", min(instrument))
print("Highest ASCII character:", max(instrument))


# --- TASK 2: THE CLEANUP CREW ---
messy_input = "   vOLUME_knob_11   "

# Remove spaces
cleaned = messy_input.strip()

# Capitalize everything
cleaned = cleaned.upper()

# Replace underscores with spaces
cleaned = cleaned.replace("_", " ")

print("\nCleaned Input:", cleaned)


# --- TASK 3: THE VALIDATOR ---
serial_number = "90210"

# Check if numeric
if serial_number.isdigit():
    print("\nValid Serial")
else:
    print("\nInvalid Serial")


# --- TASK 4: THE DUCK BRIDGE ---
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

for char in name_string:
    # 1. Display the current state of the name
    current_name = " ".join(duck_letters)
    print("There was a teacher who had a duck and Ducky was his Name-o")
    print((f"({current_name}) \n") * 3)
    print("and Ducky was his Name-o!\n")
    duck_letters[count] = "🦆"    # 2. Replacement step (Bingo Logic)
    count += 1     # 3. Increment step

# Finale
final_name = " ".join(duck_letters)
print("--- Finale! ---")
print((f"({final_name}) \n") * 3)
print("and Ducky was his Name-o!\n")
