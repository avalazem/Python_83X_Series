"""
    Name:     Mark
    Date:     January 7th, 2020
    Purpose:  Perform a swap
    Versions: First and Last
    
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Declare and initialize
x=r.randint(0,100)
y=r.randint(0,100)

#Display the Values
print("The Initial Values of x and y")
print("x = ",x)
print("y = ",y)

#Swap the values
temp=x
x=y
y=temp

#Display the Values
print("The Swapped Values of x and y")
print("x = ",x)
print("y = ",y)