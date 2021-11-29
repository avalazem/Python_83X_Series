"""
    Name:     Mark
    Date:     January 20th, 2020
    Purpose:  Ternary Operator and Relational Operators
    Versions: First and Last
    
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Randomly choose 2 variables
x=r.randint(1,10)
y=r.randint(1,10)

#Output the random variables
print("x = ",x)
print("y = ",y)

#Determine which is min and max
max=x if x >  y else y
min=x if x <= y else y

#Output the min and the max
print("max = ",max)
print("min = ",min)