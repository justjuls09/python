locked_calendar.py
"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. MONTHS is defined as a constant tuple ().
[x] 3. Program uses a for loop to display each month.
[x] 4. 'try' and 'except' blocks catch a TypeError.
[x] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""
"""
Author: Julie Gavas
Program: Locked Calendar
Purpose: Uses Constants, Tuples, and Error Handling - Locking the system
"""

# 2. DEFINE MONTHS AS A CONSTANT TUPLE (immutable collection)
MONTHS = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# 3. USE FOR LOOP TO DISPLAY EACH MONTH
print("📅 The Locked Calendar System\n")
for month in MONTHS:
    print(f"Month: {month}")

print("\nAttempting illegal modification...")

# 4. TRY/EXCEPT TO CATCH THE TYPEERROR
try:
    # TUPLES CANNOT BE CHANGED — THIS LINE ATTEMPTS TO OVERWRITE THE FIRST MONTH PRODUCING TYPEERROR
    MONTHS[0] = "Holiday Month"

except TypeError:
    # 5. EXPLAINS WHY IT FAILS
    print("ERROR: MONTHS is a constant tuple and cannot be modified.")
    print("Tuples are immutable, meaning their values are locked in place.")
