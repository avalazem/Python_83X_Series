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
a, b, c = r.randint(0,3), r.randint(0,3), r.randint(0,3)
  
# Copy value of a in min if a < b else copy b 
min = a if a <= b and a <= c else \
      b if b <= a and b <= c else c
max = a if a >= b and a >= c else \
      b if b >= a and b >= c else c
midt= a if a >= b and a <= c else \
      a if a >= c and a <= b else \
      b if b >= a and b <= c else \
      b if b >= c and b <= a else c
midm= a if b==min and c==max else \
      a if c==min and b==max else \
      b if a==min and c==max else \
      b if c==min and a==max else c
midc= (a+b+c)- min - max
  
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("The minimum of a,b,c = ", min) 
print("The middle  of a,b,c = ", midt) 
print("The middle  of a,b,c = ", midm) 
print("The middle  of a,b,c = ", midc) 
print("The maximum of a,b,c = ", max) 