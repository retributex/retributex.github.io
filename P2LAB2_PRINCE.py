# Prince Djine
# 11-13-25
# P2LAB2
# Program to use a dictionary for car MPG and calculate gas neededddd 

cars_mpg = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26, "BMW M4 Competition": 14}
# had to add the m4 comp beautiful car
keys = cars_mpg.keys()

print(keys)  # dict_keys(['Camaro', 'Prius', 'Model S', 'Silverado'])

car_choice = input("Enter a vehicle to see its mpg: ")

mpg = cars_mpg[car_choice]
print("The", car_choice, "gets", mpg, "mpg.")

miles = float(input("How many miles will you drive the " + car_choice + "? "))

gallons_needed = miles / mpg

print(gallons_needed, "gallon(s) of gas are needed to drive the", car_choice, miles, "miles.")
