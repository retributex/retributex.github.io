# Prince Djine
# 12-6,7-2025
# P5LAB - Self-Checkout Change Dispenser
# This program simulates a self-checkout machine and calculates change in dollars and coins.

import random

# Function to calculate and display change
def disperse_change(change):
    # Convert dollars to cents
    cents = int(round(change * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    print(f"\nChange is: ${change:.2f}")
    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

# Main function
def main():
    # Random total owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    # User input
    cash_given = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change_owed = round(cash_given - amount_owed, 2)

    # Display change
    disperse_change(change_owed)

# Call main
main()
