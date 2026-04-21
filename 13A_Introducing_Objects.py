#13A_Introducing_Objects.py
"""
-----------------------------------------------------------------------
ASSIGNMENT 13A: Object practice
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. Define a class using PascalCase.
[x] 3. Use __init__ to set private attributes (__variable).
[x] 4. Write Setters and Getters for the attributes.
[x] 5. Write a summary function that returns a formatted description.
[x] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

"""
Author: Julie Gavas
Program: Use __init__ to set private attributes 
Description: It will also , write setters and getters, and a summary function that returns a formatted description.
Instantiate two distinct objects and print their summaries.
"""

class Coffee:
    def __init__(self, coffee_type, size, milk, flavor, pumps):
        # Private attributes (encapsulation)
        self.__coffee_type = coffee_type
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__pumps = pumps

    # Requirement 4: Getters
    def get_coffee_type(self):
        return self.__coffee_type

    def get_size(self):
        return self.__size

    def get_milk(self):
        return self.__milk

    def get_flavor(self):
        return self.__flavor

    def get_pumps(self):
        return self.__pumps

    # Requirement 4: Setters
    def set_size(self, new_size):
        self.__size = new_size

    def set_milk(self, new_milk):
        self.__milk = new_milk

    def set_flavor(self, new_flavor):
        self.__flavor = new_flavor

    def set_pumps(self, new_pumps):
        if isinstance(new_pumps, int) and new_pumps >= 0:
            self.__pumps = new_pumps

    # Requirement 5: Summary
    def get_summary(self):
        return (
            f"Order: {self.__size} {self.__coffee_type} "
            f"with {self.__pumps} pumps of {self.__flavor}."
        )

# Requirement 6: Two objects
coffee1 = Coffee("Latte", "Large", "Whole", "Vanilla", 3)
coffee2 = Coffee("Matcha", "Medium", "Coconut", "None", 0)

print(coffee1.get_summary())
print(coffee2.get_summary())