"""
-----------------------------------------------------------------------
ASSIGNMENT 5B: THE ATM (BOSS LEVEL)
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Structure: Use match-case for main menu.
[ ] 3. Input Validation: Use .isdigit() or similar logic to prevent crashes if the user types text instead of numbers (since we are not using try-except yet).
[ ] 4. Math Safety: No overdrafts (withdrawing more than you have) and no negative deposits.
[ ] 5. Formatting: All currency must use :.2f.
-----------------------------------------------------------------------
"""

"""
Author: Julie Gavas
Program: while loops, match-case, input validation
Purpose: Create a simple ATM Machine
"""
# --- INITIAL BALANCE ---
balance = 1000.00
print(f"Your balance is: ${balance:.2f}")

# --- MAIN LOOP ---
while True:
    print("\n======  ATM MENU  ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Funds")
    print("5. Exit")
   

    choice = input("Select an option (1-5): ")

    match choice:

        # --- CHECK BALANCE ---
        case "1":
            print(f"Your balance is: ${balance:.2f}")

        # --- DEPOSIT ---
        case "2":
            amount = input("Deposit amount: ")

            if amount.replace(".", "", 1).isdigit():
                amount = float(amount)
                if amount > 0:
                    balance += amount
                    print(f"Deposited! New balance: ${balance:.2f}")
                else:
                    print("Amount must be positive.")
            else:
                print("Please enter a number.")

        # --- WITHDRAW ---
        case "3":
            amount = input("Withdraw amount: ")

            if amount.replace(".", "", 1).isdigit():
                amount = float(amount)
                if amount > balance:
                    print("Not enough money.")
                elif amount <= 0:
                    print("Amount must be positive.")
                else:
                    balance -= amount
                    print(f"Withdrawn! New balance: ${balance:.2f}")
            else:
                print("Please enter a number.")

        # --- TRANSFER ---
        case "4":
            amount = input("Transfer amount: ")

            if amount.replace(".", "", 1).isdigit():
                amount = float(amount)
                if amount > balance:
                    print("Not enough money.")
                elif amount <= 0:
                    print("Amount must be positive.")
                else:
                    balance -= amount
                    print(f"Transferred! New balance: ${balance:.2f}")
            else:
                print("Please enter a number.")

        # --- EXIT PROGRAM ---
        case "5":
            print("Goodbye!")
            break

        # --- INVALID MENU OPTION ---
        case _:
            print("Invalid Selection.")