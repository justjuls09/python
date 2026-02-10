"""
-----------------------------------------------------------------------
DEMO: The Softball Strategizer (Assignment 4A Logic)
AUTHOR: Julie Gavas
PURPOSE: Demonstrating AND, OR, NOT,ELIF branching and the modulus (%) operator using softball actions and number
categorization.
-----------------------------------------------------------------------
"""

# --- THE CAST ---
person = "Julie"
person2 = "Alex"
player = "The Batter"

# --- THE "VOCABULARY" ---
ACTION_BUNT = 1
ACTION_HIT_LEFT = 2
ACTION_HIT_RIGHT = 3
ACTION_HIT_MIDDLE = 4
ACTION_POP_OUT = 5
ACTION_HOMERUN = 6

print(f"🥎 {player} steps up to the plate. The crowd is watching closely.")
print(f"🥎 {player} looks toward {person} in the dugout for the signal.")
print(f"🥎 {player} glances at {person2} coaching at third base.")
print("-" * 40)

# --- GETTING USER INPUT ---
print("Help us figure out what the batter should do!")
choice_1 = int(input("First action (Pick 1-6): "))
choice_2 = int(input("Second action (Pick 1-6): "))

inning = int(input("Enter the current inning number: "))
run_diff = int(input("Enter the run differential (your score - opponent score): "))

print("-" * 40)

# --- MODULUS (%) --- 
# Use % to determine if the inning is even or odd
if inning % 2 == 0:
	print(f"\n⚾ Inning {inning} is even — {person2} yells: 'Even innings are where we step it up!'")
else:
    	print(f"\n⚾ Inning {inning} is odd — {person} shouts: 'Odd innings are where momentum shifts!'")

print("-" * 40)

# --- RUN DIFFERENTIAL CATEGORIZATION --- 
if run_diff > 0:
    print("📈 We're winning! Keep the pressure on!")
elif run_diff < 0:
    print("📉 Time for a comeback! Rally caps on!")
else:
    print("⚖️ It's a tie ballgame! Every pitch matters now!")

print("-" * 40) 

# --- THE LOGIC GATE ---

# 1. Using OR
if choice_1 == ACTION_BUNT or choice_1 == ACTION_HIT_LEFT:
	print(f"\n📣 The batter is trying to advance the runner!")
    	print(f"   {person} shouts: 'Smart move — way to play ball!'")

# 2. Using AND
elif choice_1 == ACTION_HIT_MIDDLE and choice_2 == ACTION_HOMERUN:
    	print(f"\n💥 Power combo! A line drive followed by a bomb.")
    	print(f"   {person2} yells: 'That’s how you take control of the inning!'")

elif (choice_1 % 2 == 0) or (choice_2 % 2 == 0):
    print("\n🔢 Alex shouts: 'At least one of those choices is an even‑number strategy!'")

# 3. Using ELIF
elif choice_1 == ACTION_POP_OUT:
    	print(f"\n😬 The batter pops it straight up.")
    	print(f"   {person} sighs: 'We’ll get the next one.'")

elif choice_1 == ACTION_HOMERUN:
    	print(f"\n🔥 The batter crushes it over the fence!")
    	print(f"   {person2} jumps up: 'Touch 'em all!'")

# 4. Using NOT
elif not (choice_1 >= 1 and choice_1 <= 6):
    	print(f"\n🚫 That’s not a valid softball action! The ump looks confused.")

# 5. Default
else:
    	print(f"\n🤔 The play is unclear. The batter adjusts their helmet and waits.")

print("-" * 40)
