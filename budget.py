#budget.py
"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# Get information from the user
# Ask user for Monthly Income (float).
income = float(input("Enter your Monthly Income: $"))

# Ask user for 5 DIFFERENT expense amounts (float).

rent = float(input("Enter your Monthly Rent Expense: $"))
utilities = float(input("Enter your Monthly Utilities Expense: $")) 
groceries = float(input("Enter your Monthly Groceries Expense: $"))
transportation = float(input("Enter your Monthly Transportation Expense: $"))
entertainment = float(input("Enter your Monthly Entertainment Expense: $"))

# Calculate Total Expenses and Remaining Balance.
total_expenses = rent + utilities + groceries + transportation + entertainment
remaining_balance = income - total_expenses

# Calculate Percentage of Income Spent.
percentage_spent = total_expenses / income

# Output formatted to 2 decimal places (:,.2f or :.2%).
print("\n----- Budget Summary -----")
print(f"\nTotal Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {percentage_spent:.2%}")
# Example Output:
# Total Expenses: $2,500.00
# Remaining Balance: $1,500.00
# Percentage of Income Spent: 62.50%
# Suggested inputs for testing:
# Monthly Income: 4000
# Rent Expense: 1200
# Utilities Expense: 300
# Groceries Expense: 500
# Transportation Expense: 200
# Entertainment Expense: 300







