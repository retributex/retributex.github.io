# Prince Djine
# 11-15-2025
# P2HW2
# Collect grades for 6 modules and display lowest, highest, sum, and average
# Pseudocode:
# 1. Ask user to input grades for Module 1 to Module 6 (store as floats)
# 2. Store all grades in a list called module_grades
# 3. Find the lowest grade in the list using min()
# 4. Find the highest grade in the list using max()
# 5. Calculate sum of grades using sum()
# 6. Calculate average by dividing sum by number of grades
# 7. Display results in formatted output with equal dashes

# --- USER INPUTS ---
print("Please enter your grades for the following modules:")
print()

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))
print()

# --- STORE GRADES IN LIST ---
module_grades = [grade1, grade2, grade3, grade4, grade5, grade6] # wasn't working earlier fi this entire line

# --- CALCULATIONS ---
lowest_grade = min(module_grades)
highest_grade = max(module_grades) # the grade we all need
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / 6

# --- OUTPUT ---
print("-----------Results-----------")   # equal length dashes
print("Lowest Grade:   {:.2f}".format(lowest_grade))
print("Highest Grade:  {:.2f}".format(highest_grade))
print("Sum of Grades:  {:.2f}".format(sum_of_grades))
print("Average:        {:.2f}".format(average_grade))
print("-----------------------------")   # equal length dashes whooop
