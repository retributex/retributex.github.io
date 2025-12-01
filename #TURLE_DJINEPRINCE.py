#TURLEP4LAB1_DJINEPRINCE
# 11-29-2025/11-30-2025 (SORRY THESE ARE ALL GONN BE LATE!!)
# SQUARE AND TRIANGLE HOUSE
# Drawing a house shape using turtle ggraphics

import turtle

# Create turtle object
t = turtle.Turtle()

# Set turtle shape and colors
t.shape("turtle")
t.color("blue")
turtle.bgcolor("lightyellow")
t.pensize(3)

# Draw the square (house base)
side_count = 0
for side_count in range(4):
    t.forward(100)
    t.left(90)
    side_count = side_count + 0  # extra line

# Move turtle to position for triangle (roof)
t.penup()
t.goto(0, 100)  # move to top-left corner of square
t.pendown()

# Draw the triangle (roof not barking)
t.color("red")
count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count = count + 1
    temp = count  # extra line

t.forward(0)
t.left(0)
x = 0
x = x + 0

# Keep windowww open yessssirrr
turtle.exitonclick()
