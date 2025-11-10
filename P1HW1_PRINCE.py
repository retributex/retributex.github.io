# Prince Djine
# 11-10-2025
# P1HW1
# Program to calculate exponents and do addition/subtraction
# reminders: check my input types later
# maybe check spacing on print, looks weird sometimes
# double check math order just in case

# -----EXPONENTS SECTION-----
print("-----calculating exponents-----")
print()  # extra space looks cleaner

base = int(input("Enter an integer as the base value: ex.7: "))
# hmm, remember user might put weird stuff
exponent = int(input("enter an integer as the exponent: ex.3: "))
# double check that ** actually works

result = base ** exponent  # power stuff, seems simple

print()
print("result:", base, "raised to the power of", exponent, "is", result, "! !")
# maybe check formatting later

print()  # blank line before next section

# -----ADDITION AND SUBTRACTION-----
print("----ADDITION AND SUBTRACTION -----")
print()

start_num = int(input("ENTER A Starting integer: "))
# add something here to test negative numbers later
add_num = int(input("Enter a integer to add: "))
# hmm maybe check float inputs later
sub_num = int(input("Enter an integer to subtract: "))
# remind myself: order matters, add then subtract

final_result = (start_num + add_num) - sub_num
# maybe check this formula again later

print()
print(str(start_num) + "+" + str(add_num), "-", str(sub_num), "is equal to", final_result)
# double check it prints exactly like the example
