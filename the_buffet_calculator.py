"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [February 2, 2026]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""
# Get the user's age
age = int(input("Please enter your age: "))
# Determine the buffet price based on age
# Use if/elif/else to determine price
if age < 1:
    price = 0.00
elif 1 <= age <= 11:
    price = age * 1.00
elif 12 <= age <= 64:
    price = 16.95
else:
    price = 12.95
# Print the final price formatted as currency
print(f"For your age ({age}) the buffet price is: ${price:,.2f}")
# Example Outputs:
# Age: 0  -> Price: $0.00
# Age: 7  -> Price: $7.00
# Age: 44 -> Price: $16.95
# Age: 77 -> Price: $12.95
# Suggested inputs for testing:
# Age: 0
# Age: 7
# Age: 44
# Age: 77
