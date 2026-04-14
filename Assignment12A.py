"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. PHASE 1: External menu_config.txt file created in workspace.
[x] 3. Program reads and parses the .txt file into a Dictionary.
[x] 4. PHASE 2: break the dictionary into individual variables.
[x] 6. Print each category and its details
[x] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

"""
Author: Julie Gavas
Program: The Configurable Menu & Auditor
Description:
Reads an external menu configuration file, parses it into a dictionary,
breaks it into individual variables, prints each category, and audits
the PRICES category using string-to-float conversion.
"""

CONFIG_FILE = "menu_config.txt"


def load_menu_config(filename):
    """
    Reads the menu_config.txt file using 'r' mode.
    Parsing pipeline: strip() -> split(';')
    Also converts PRICES values into floats safely (ValueError protected).
    """
    menu_dict = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(";")
                if len(parts) != 2:
                    continue

                category = parts[0].strip().upper()
                detail = parts[1].strip()

                # --- CONVERSION LOGIC (String -> Float) ---
                if category == "PRICES":
                    # Expect something like: Small=3.00, Medium=4.00, Large=5.00
                    price_list = []
                    price_items = detail.split(",")

                    for p in price_items:
                        p = p.strip()

                        # If format is "Small=3.00", split on "=" and take the number
                        if "=" in p:
                            number_str = p.split("=")[1].strip()
                        else:
                            # If format is just "3.00", use it directly
                            number_str = p

                        try:
                            price_list.append(float(number_str))
                        except ValueError:
                            # Type Trap Shield: corrupted data won't crash the program
                            continue

                    menu_dict[category] = price_list
                else:
                    menu_dict[category] = detail

    except FileNotFoundError:
        print(f"\nERROR: The file '{filename}' was not found.")
        print("Make sure menu_config.txt is in the same folder as this program.\n")
        return None

    return menu_dict


def split_into_variables(menu_dict):
    """Breaks the dictionary into individual category variables."""
    coffee = menu_dict.get("COFFEE")
    prices = menu_dict.get("PRICES")   # this will be a LIST of floats now
    milk = menu_dict.get("MILK")
    flavors = menu_dict.get("FLAVORS")
    toppings = menu_dict.get("TOPPINGS")
    return coffee, prices, milk, flavors, toppings



def print_category(title, detail):
    """Prints a single menu category and its items."""
    print(f"\n{title}")

    if detail is None:
        print("\t(Missing category)")
        return

    # PRICES: detail is a list of floats
    if isinstance(detail, list):
        for price in detail:
            print(f"\t${price:.2f}")   # this is the money formatting
        return

    # All other categories
    items = detail.split(",")
    for item in items:
        print(f"\t{item.strip()}")



def print_menu(coffee, prices, milk, flavors, toppings):
    """Prints all menu categories."""
    print("\n==============================")
    print("     CONFIGURABLE MENU")
    print("==============================")

    print_category("COFFEE", coffee)
    print_category("PRICES", prices)
    print_category("MILK", milk)
    print_category("FLAVORS", flavors)
    print_category("TOPPINGS", toppings)

    print("\n==============================\n")


def audit_prices(prices):
    """
    Auditor requirement: sums numeric price data after float conversion.
    """
    if prices is None or not isinstance(prices, list):
        print("AUDIT: No valid prices found to audit.")
        return

    total = 0.0
    for p in prices:
        total += p

    print("AUDIT RESULTS")
    print("------------")
    print(f"Total of PRICES values = ${total:.2f}\n")


def main():
    menu_dict = load_menu_config(CONFIG_FILE)
    if menu_dict is None:
        return

    coffee, prices, milk, flavors, toppings = split_into_variables(menu_dict)
    print_menu(coffee, prices, milk, flavors, toppings)

    # Required audit behavior: show that float conversion works with math
    audit_prices(prices)


main()