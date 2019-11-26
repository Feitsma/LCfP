#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:04:04 2019

@author: hielke
"""


"""
Exercise 2.5, page 7
"""
#two_Power_17 = 512
#pi_6decimals = 3.141592
#print("2^17 is" , two_Power_17)
#print("Pi with 6 decimals is", pi_6decimals)

"""
Exercise 2.5, page 8/10

import math
#a = 1
#b = 5
#c = 6
a = int(input("Enter the value of a as real number:"))
b = int(input("Enter the value of b as real number:") )
c = int(input("Enter the value of c as real number:") )


d = b**2 - 4*a*c
square_root_of_d = math.sqrt(d)
sol1 = (-b - square_root_of_d)/(2*a)
sol2 = (-b + square_root_of_d)/(2*a)
print("solution 1 is:", sol1)
print("solution 2 is:", sol2)
"""

"""
Exercise 2.6, page 11

with open("storage.txt") as file_handler:
    file_content = str(file_handler.read())
print(file_content)
print(type(file_content))
print(type(file_handler))
"""

"""
Exercise 2.7, page 12/13
"""
born = int(1963)
weighs = float(94.3)
personal_data = list(("Nick", born, weighs))
print(personal_data)
to_grow = []
print(type(to_grow))
print(to_grow)
to_grow.append("first element added")
to_grow.append(int(2))
to_grow.append("third element added")
print(to_grow)
x = to_grow.__class__
print("the attribute __class__ of the 'to_grow' object is:", x)
y = to_grow.append("4th element added")
print("the returned value from append() is a:", y)
print(to_grow)