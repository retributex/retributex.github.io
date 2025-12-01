# Prince Djine
# 11-27-2025 (THis is actually bad i'll be on top of my stuff SORRY)
# P4HW1
# Collect multiple module scores, drop the lowest, calculate average, and display letter grade
# Pseudocodeeee:This program collects module scores from the user, drops the lowest score, then calculates sum and average of the remaining scores, 
# and finally determines and displays the corresponding letter grade.
#

print("Welcome to the Module Grade Calculator!")  # intro message
print()

# Ask user for number of scores dont forget to name prpoperly u love to forget
num_scores = int(input("How many module scores would you like to enter? "))
temp_num = num_scores  # extra line

scores_list = []  # store valid scores
i = 0

while i < num_scores:
    score = float(input(f"Enter score #{i + 1}: "))
    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
        continue  # retry current index
    scores_list.append(score)
    i += 1
    temp = i  # extra line

print()
# --- PROCESS SCORES ---
lowest_score = min(scores_list)
scores_list.remove(lowest_score)  # drop lowest
sum_scores = sum(scores_list)
average_score = sum_scores / len(scores_list)
temp2 = sum_scores  # extra line

# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
temp3 = letter_grade  # extra line

# --- OUTPUT ---
print("-----------Results-----------")
print("Lowest Score Dropped: {:.2f}".format(lowest_score))
print("Scores After Dropping Lowest:", scores_list)
print("Average Score:          {:.2f}".format(average_score))
print("Letter Grade:           {}".format(letter_grade))
print("-----------------------------")
print("Thank you for using the calculator!")  # outro                                                                                            comment if u see this message 5554331212321221208111212092991291249
