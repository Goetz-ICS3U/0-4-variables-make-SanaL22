"""
# Author: Sana Laone
# Date: February 24, 2026
# Discription: calculate the area and perimeter of a cricle, rectangle and octagon
"""
# Input
circle_radius = int(input("The radius of the circle: "))
rectangle_lenght = int(input("The length of the rectangle: "))
rectangle_width = int(input("The width of the rectangle: "))
octagon_side = int(input("A side length of the octagon: "))

import math

circle_area = math.pi * circle_radius **2
circles_perimeter = 2 * math.pi * circle_radius

rectangle_area = rectange_lenght * rectangle_width
rectangle_perimeter = 2 * (rectange_lenght + rectangle_width)

octagon_area = 2 * (1 + math.sqrt(2)) * octagon_side ** 2
octagon_perimeter = 8 * octagon_side


# Processing / Output
print(f"The circle has an area of {circle_area} and a perimeter of {circles_perimeter}")
print(f"The rectangle has an area of {rectangle_area} and a perimeter of {rectangle_perimeter}")
print(f"The octagon has an area of {octagon_area} and a perimeter of {octagon_perimeter}")