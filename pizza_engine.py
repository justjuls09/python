"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[x] 3. Function 'make_pizza' defines 4 specific parameters.
[x] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[x] 5. main() displays the Global Pantry list to the user.
[x] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# -----------------------------
# GLOBAL PANTRY
# -----------------------------
TOPPINGS = ("Pepperoni", "Onions", "Sausage", "Green Peppers")


# -----------------------------
# ARCHITECT FUNCTION
# -----------------------------
def make_pizza(customer, size, topping, is_delivery=False):
    """
    Builds and displays a pizza order summary.
    """
    print("\n--- ORDER SUMMARY ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")

    if is_delivery:
        print("Delivery: Yes")
    else:
        print("Delivery: No")

    print("----------------------\n")


# -----------------------------
# MAIN FUNCTION (THE CONDUCTOR)
# -----------------------------
def main():
    print("Welcome to Joplin's Pizza Engine!\n")

    # Requirement 5: Display the Global Pantry list
    print("Available Toppings:")
    for item in TOPPINGS:
        print(f"- {item}")

    # -----------------------------
    # VALIDATION LOOPS - per Jeanie's suggestion.
    # -----------------------------

    # Customer name (cannot be blank)
    while True:
        customer_name = input("\nEnter your name: ").strip()
        if customer_name != "":
            break
        print("Error: Name cannot be blank.")

    # Pizza size (must be one of the allowed options)
    valid_sizes = ("Small", "Medium", "Large")
    while True:
        pizza_size = input("Choose a size (Small, Medium, Large): ").title()
        if pizza_size in valid_sizes:
            break
        print("Error: Please choose Small, Medium, or Large.")

    # Topping (must be in TOPPINGS)
    while True:
        pizza_topping = input("Choose a topping from the list above: ").title()
        if pizza_topping in TOPPINGS:
            break
        print("Error: Please choose a topping exactly as shown.")

    # Delivery (must be yes/no)
    while True:
        delivery_choice = input("Is this for delivery? (yes/no): ").lower()
        if delivery_choice in ("yes", "no"):
            delivery_flag = delivery_choice == "yes"
            break
        print("Error: Please type 'yes' or 'no'.")

    # Requirement 6: Keyword-argument function call
    make_pizza(
        customer=customer_name,
        size=pizza_size,
        topping=pizza_topping,
        is_delivery=delivery_flag
    )


# -----------------------------
# CALL MAIN
# -----------------------------
main()
