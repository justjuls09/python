"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

"""
Author: Julie Gavas
Program: While loop
Purpose: Create a registration form.  All inputs use the while loops for
validation and use the correct Boolean logic with the .upper() 	
"""

print("Welcome to the Field Trip Registration Form!")
print("-" * 55)

# -------------------------------
# FIRST NAME (cannot be blank)
# -------------------------------
first_name = input("Enter your first name: ").strip()

while first_name == "":
    print("First name cannot be blank.")
    first_name = input("Enter your first name: ").strip()

# -------------------------------
# LAST NAME (cannot be blank)
# -------------------------------
last_name = input("Enter your last name: ").strip()

while last_name == "":
    print("Last name cannot be blank.")
    last_name = input("Enter your last name: ").strip()

# -------------------------------
# CHAPERONE (Y/N only)
# -------------------------------
chaperone = input("Is a parent volunteering to be a chaperone? (Y/N): ").strip().upper()

while chaperone not in ("Y", "N"):
    print("Please enter only Y or N.")
    chaperone = input("Are you a chaperone? (Y/N): ").strip().upper()

# -------------------------------
# PHONE NUMBER (cannot be blank)
# -------------------------------
phone = input("Enter your phone number: ").strip()

while phone == "":
    print("Phone number cannot be blank.")
    phone = input("Enter your phone number: ").strip()

# -------------------------------
# VALIDATE TICKET COUNT (MUST BE AN INTEGER)
# Crash-proofing your numbers
# -------------------------------
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break # Valid number! Escape the loop!
        print("❌ Error: Must be at least 1 ticket.")
    except ValueError:
        print("❌ Error: Please enter a NUMBER (e.g., 5, not 'five').")

print(f"✅ Ordered {tickets} tickets.")

print("-" * 55)
print("Registration Complete!")
print(f"Name: {first_name} {last_name}")
print(f"Chaperone: {chaperone}")
print(f"Phone: {phone}")
print(f"Tickets Requested: {tickets}")
print("-" * 55)
