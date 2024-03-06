# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:52:41 2024

@author: vitug
"""

"""1. Write a Python class to reverse a string word by word.
Example:
Input string : 'hello .py'
Expected Output : '.py hello'"""
class reverse:
    def words(self, s):
         return ' '.join(reversed(s.split()))
print(reverse().words('hello .py'))
print(reverse().words('reverse Python code displayed'))


"""2. Write a Python class named Circle constructed by a radius and two methods which 
will compute the area and the perimeter of a circle."""
from math import pi
class Circle():
    def __init__(self):
        self.radius = float(input("Enter radius of a circle: "))

    def area(self):
        print("the area of a circle is: ", pi * self.radius * self.radius)
        
    def perimeter(self):
        print("The perimeter of this circle is: ", 2 * pi * self.radius)

circle_object = Circle()
circle_object.area()
circle_object.perimeter()
