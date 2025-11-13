# Prince Djine
# November 13, 2025
# P2LAB1
# This program asks for the radius of a circle and shows
# the diameter, circumference, and area (remind urself to test diff numbers later)

# ask user for radius
radius = float(input("What is the radius of the circle? "))

# using pi without import
pi = 3.14159

# do the math
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius  # might change this later if needed

# print everything
print()
print("The diameter of the circle is", diameter)
print()
print("The circumference of the circle is", circumference)
print()
print("The area of the circle is", area)
# check results for radius 8.75 later
