# P3LAB_LastnameFirstname.py
# CTI-110 P3LAB
# Author: Your Name
# Date: YYYY-MM-DD
# Description: This program calculates the most efficient number of dollars,
# quarters, dimes, nickels, and pennies for a given amount of money.

# Get input from user
amount = float(input("Enter the amount of money as a float: $"))

# Convert amount to cents for easier calculation
cents = int(round(amount * 100))

# Initialize coin/dollar counters
dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents  # remaining cents

# Display the result
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
else:
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else ''}")
