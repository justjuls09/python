"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
"""
Author: Julie Gavas
Program: Ticket sales
Purpose: Create a list, check the list against seats taken or non-existent
"""
# 1. --- THE LIST OF 20 SEATS ---

seats = list(range(1,21))

print("🎟️ Welcome to the Theater Ticket Kiosk!")

# 6. ---  REPEAT UNTIL USER QUITS OR SEATS ARE EMPTY ---
while True:

    # ---  STOP IF NO SEATS ARE AVAILABLE ---
    if len(seats) == 0:
        print("\nSorry,all seats are sold out!")
        break

    # 2. ---  DISPLAY THE LIST OF AVAILABLE SEATS ---
    print("\nAvailable seats:", seats)
    
    # SIMPLE LOOP USING END=" " TO KEEP SEATS ON ONE LINE(JEANIE'S PROFESSIONAL TIP)

    for seat in seats:		# NAMING VARIABLES

        print(seat, end=" ")
    print()	# MOVE TO THE NEXT LINE

    # 3. ---  ASK USER FOR SEAT NUMBER (0 TO QUIT) ---
    choice = input("Enter a seat number to buy (0 to quit): ")

    # ---  VALIDATION - MUST BE A NUMBER ---
    if not choice.isdigit():
        print("Please enter a valid NUMBER.")
        continue

    choice = int(choice)

    # ---  EXIT CONDITION ---
    if choice == 0:
        print("Goodbye!")
        break

    # 5. --- CHECK FOR INVALID ---
    if choice in seats:
        seats.remove(choice)   # 4. ---  REMOVE SELECTED SEAT FROM THE LIST  ---
        print(f"Seat {choice} sold!")
    else:
        print("That seat is not available. Try again.")
