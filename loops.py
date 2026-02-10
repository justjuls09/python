"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
Author: Julie Gavas
Program: Loop Demonstration
Purpose: demonstrates:
    - A while loop controlled by a Boolean variable.
    - A for loop that counts backward from 99.
"""

# ---------------------------------------------------------
# TASK 1: WHILE LOOP — "THE NAGGING KID"
# ---------------------------------------------------------

print("TASK 1: The Nagging Kid\n")

# Boolean variable controls the loop
still_asking = True

while still_asking:
    response = input("Are we there yet? ").lower()

    if response == "yes":
        still_asking = False
        print("Finally! We are here!\n")
    else:
        print("...sigh...")

# ---------------------------------------------------------
# TASK 2: FOR LOOP — "99 BOTTLES OF BEER"
# ---------------------------------------------------------

print("TASK 2: 99 Bottles of Beer\n")

for bottle in range(99, 0, -1):
    print(f"{bottle} bottles of beer on the wall!")
