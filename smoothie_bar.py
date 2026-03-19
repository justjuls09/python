"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
[x] 1. Header Docstring included.
[x] 2. Global Constants BASES and FRUITS defined as Tuples.
[x] 3. Professional function get_price(size) returns a float.
[x] 4. Professional function blend(size, base, fruit, scoops) for output.
[x] 5. main() function handles try/except for scoops (int).
[x] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""
"""
Author: Julie Gavas
Program: smoothie_bar.py
Purpose:
    A functional-programming style smoothie ordering system.
    Demonstrates reusable functions, global constants, input validation,
    and clean, professional output formatting.

"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


def get_price(size):
    """
    RETURNS THE BASE PRICE OF A SMOOTHIE BASED ON SIZE.
    """
    size = size.lower()

    if size == "small":
        return 3.00
    elif size == "medium":
        return 4.00
    elif size == "large":
        return 5.00
    else:
        return 0.00


def blend(size, base, fruit, scoops):
    """
    THIS FUNCTION PRINTS THE SMOOTHIE SUMMARY.
    """
    price = get_price(size)

    print("\n--- Smoothie Summary ---")
    print(f"Size:   {size}")
    print(f"Base:   {base}")
    print(f"Fruit:  {fruit}")
    print(f"Protein Scoops: {scoops}")
    print(f"Total Price: ${price:.2f}")
    print("-------------------------")


def main():
    """
    Main program logic:
    - Welcomes the user
    - Gathers all smoothie ingredients
    - Validates scoops using try/except (Naked Input Rule)
    - Calls get_price() to retrieve the calculation
    - Calls blend() to print the production ticket
    """

    # 1. WELCOME
    print("Welcome to the Smoothie Bar!\n")

    # 2. ORDER
    user_size = input("Choose a size (Small, Medium, Large): ")

    print("\nAvailable Bases:")
    for b in BASES:
        print("-", b)
    user_base = input("Choose a base: ")

    print("\nAvailable Fruits:")
    for f in FRUITS:
        print("-", f)
    user_fruit = input("Choose a fruit: ")

    # 3. INPUT (Resilience Check)
    while True:
        try:
            user_scoops = int(input("\nHow many protein scoops? "))
            break
        except ValueError:
            print("Numbers only, please!")

    # 4. CALCULATION 
    smoothie_price = get_price(user_size)

    # 5. PRODUCTION TICKET
    blend(user_size, user_base, user_fruit, user_scoops)

main()