# Prince Djine 
# 11-20-2025
# P3HW1 Debuggingggggggggggggggggggggggg
# This program takes 6 grades, finds the lowest, highest, sum,
# average, and displays the letter grade.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# calc values (verify ts with old code p2hw2)
low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg = sum_grades / 6

# Output resultss n stuff67

print("-------------Results-----------")
print("Lowest Grade:         ", low)
print("Highest Grade:        ", high)
print("Sum of Grades:        ", sum_grades)
print("Average:              ", round(avg, 2))
print("--------------------------------")

# Determine letter grade k
if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg >= 70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F')