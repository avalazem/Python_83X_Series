"""
    Name:     Mark
    Date:     January 20th, 2021
    Purpose:  Ternary Operator and Relational Operators
    Versions: First and Last
    
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
a, b = r.randint(0,3), r.randint(0,3)
  
# Copy value of a in min if a < b else copy b 
min = a if a <= b else b
max = a if a >= b else b
  
print("a = ",a)
print("b = ",b)
print("The minimum of a,b = ", min) 
print("The maximum of a,b = ", max) 
