# P4HW2_DJINEPRINCE
# 11-29-2025/11-30-2025/12-1-2025
# P4HW2 Multiple Employee Salary Calculator
# Calculate regular, overtime, and gross pay for multiple employees and show totals
# Pseudocode:
# 1. Initialize totals and employee count
# 2. While True, get employee name; break if "Done"
# 3. Get hours worked and pay rate
# 4. Calculate overtime and regular pay
# 5. Add to running totals and increment employee count
# 6. Display individual pay info
# 7. After loop ends, display totals

# --- INITIALIZE TOTALS ---
total_regular = 0
total_overtime = 0
total_gross = 0
employee_count = 0

temp = 0 

# --- MAIN LOOP FOR MULTIPLE EMPLOYEES ---
while True:
    name = input("Enter employee's name (or Done to quit): ")
    if name == "Done":
        break  # exit loop if sentinel entered

    hours = float(input("Enter number of hours worked: "))
    rate = float(input("Enter employee's pay rate: "))

    temp2 = 0

    # --- CALCULATE PAY ---
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay

    # --- UPDATE TOTALS ---
    total_regular += regular_pay
    total_overtime += overtime_pay
    total_gross += gross_pay
    employee_count += 1

    temp3 = employee_count  # temporary variable to hold employee count
    # --- DISPLAY INDIVIDUAL EMPLOYEE PAY ---
    print("--------------------------------------------")
    print("Employee Name:", name)
    print("Hours worked  Pay Rate    OverTime    Overtime Pay    RegHour Pay     Gross Pay")
    print("--------------------------------------------------------------------------------")
    print("{:<13} ${:<10.2f} {:<10} ${:<14.2f} ${:<14.2f} ${:<.2f}".format(
        hours, rate, overtime_hours, overtime_pay, regular_pay, gross_pay
    ))
    print("--------------------------------------------")
    print()  # extra space

# --- DISPLAY TOTALS AFTER LOOP ---
print("************ PAY TOTALS ************")
print("Number of employees processed:", employee_count)
print("Total Regular Pay:  ${:.2f}".format(total_regular))
print("Total Overtime Pay: ${:.2f}".format(total_overtime))
print("Total Gross Pay:    ${:.2f}".format(total_gross))
print("***********************************")
