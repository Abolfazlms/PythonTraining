"""This program recives the radius of a circle from the user and calculates its area"""
from math import pi
radius = float(input("Enter The radius of circle: "));
print(f"Area of circle with radius {radius:0.0f} is : {pi*(radius**2)}");