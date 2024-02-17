# Program to calculate the quantity of paint need for painting a wall
import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


# Height of wall (m)
test_h = int(input("Enter the HEIGHT of the wall:\n"))
# Width of wall (m)
test_w = int(input("Enter the WIDTH of the wall:\n"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)