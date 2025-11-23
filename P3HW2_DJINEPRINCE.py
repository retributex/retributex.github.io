# P3HW2_DJINEPRINCE
# 11-21-2025
# P3HW2 Salary Calculator
# This program asks for an employee's hours and pay rate,
# calculates regular pay, overtime pay, and gross pay.
#had to resubmit forgot to change file name and stuff
# Pseudocode:
# 1. Get employee name, hours worked, and pay rate.
# 2. If hours > 40, calculate overtime hours and overtime pay (1.5 × rate).
#    Otherwise, overtime hours = 0.
# 3. Compute regular pay and gross pay.
# 4. Display all values using formatted columns.

# ----- USER INPUTS -----
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# ----- CALCULATIONS -----
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 * rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours * rate

gross_pay = regular_pay + overtime_pay

# ----- OUTPUT -----
print("------------------------------------------")
print("Employee Name:", name)

print("Hours worked  Pay Rate    OverTime    Overtime Pay    RegHour Pay     Gross Pay")
print("-----------------------------------------------------------------------------------")

# Lined-up formatting (using .format exactly like taught in classsss hopewfully #braingrowing)
print("{:<13} ${:<10.2f} {:<10} ${:<14.2f} ${:<14.2f} ${:<.2f}".format(
    hours, rate, overtime_hours, overtime_pay, regular_pay, gross_pay
))
