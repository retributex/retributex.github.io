# P4LAB2_DJINEPRINCE
# 11-30-2025
# MULTIPLICATION TABLE WITH LOOPING, Repeat asking user for a number, show multiplication table if non-negative, else warn, until user says no


run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: ")) # get that input 

    if number < 0:
        print("This program does not handle the negative number.") # get that negative junk outta here
    else:
        print(f"Multiplication Table for {number}")
        for i in range(1, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
            temp = result  # extra line

    run_again = input("Would you like to run the program again? (yes/no): ")
    temp2 = run_again  

print("Program ended. Thank you!")
