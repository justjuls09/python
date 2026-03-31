#menu_file.py
"""
-----------------------------------------------------------------------
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Joplin's Pizza Engine (V3.0)
Developer: Julie Gavas
-----------------------------------------------------------------------
"""

# -----------------------------
# GLOBAL CONSTANTS (Pantry Rules)
# -----------------------------
MENU_FILE = "pizza_menu.txt"
TOPPINGS = ("Pepperoni", "Onion", "Sausage", "Green Peppers")
SIZES = ("Small", "Medium", "Large")


# -----------------------------
# ARCHITECT FUNCTION
# -----------------------------
def make_pizza(customer="Guest", size="Medium", topping="Pepperoni", is_delivery=False):
    """
    Builds and displays a pizza order summary.
    Default values ensure the system never crashes from missing data.
    """
    print("\n--- ORDER SUMMARY ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Delivery: {'Yes' if is_delivery else 'No'}")
    print("----------------------\n")


# -----------------------------
# MAIN FUNCTION (THE CONDUCTOR)
# -----------------------------
def main():
    print("Welcome to Joplin's Pizza Engine!\n")

    # Display Global Pantry
    print("Available Toppings:")
    for item in TOPPINGS:
        print(f"- {item}")

    # Ingestion Phase (with defaults if blank)
    name = input("\nEnter your name: ").title() or "Guest"

    size = input("Choose a size (Small, Medium, Large): ").title()
    if size not in SIZES:
        size = "Medium"  # default

    topping = input("Choose a topping from the list above: ").title()
    if topping not in TOPPINGS:
        topping = "Pepperoni"  # default

    delivery_choice = input("Is this for delivery? (yes/no): ").lower()
    is_delivery = delivery_choice == "yes"

    # Keyword Argument Handoff
    make_pizza(
        customer=name,
        size=size,
        topping=topping,
        is_delivery=is_delivery
    )


# -----------------------------
# CALL MAIN
# -----------------------------
main()