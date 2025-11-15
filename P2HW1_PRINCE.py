# Prince Djine
# 11-15-2025
# P2HW1
# Format travel expenses in a clean way using string formatting
# remember this builds off P1HW2 but just changes the output look

print("This program calculates and displays Travel Expenses!")
print()

# --- USER INPUTS ---
budget = float(input("Enter your initial budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("Enter amount for gas: "))
print()
accommodation = float(input("Enter your approximate amount for accommodation: "))
print()
food = float(input("Lastly, enter how much you'll need for food: "))
print()

# --- CALCULATIONS ---
total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

# --- OUTPUT (formatted like assignment example) ---
print("----------Travel Expenses-----------")   # 35 dashes
print("Location:       {}".format(destination))
print("Initial Budget: ${:.2f}".format(budget))
print("Fuel:           ${:.2f}".format(gas))
print("Accomodation:   ${:.2f}".format(accommodation))
print("Food:           ${:.2f}".format(food))
print("-------------------------------------")   # also 35 dashes
print("Remaining Balance: ${:.2f}".format(remaining_budget))

# reminder: test with different numbers to make sure it lines up
# post it lineeeeez upp[]