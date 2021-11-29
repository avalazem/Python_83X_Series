# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:23:54 2020

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
a, b, c = r.randint(0,21), r.randint(0,21), r.randint(0,21)
  
# Copy value of a in min if a < b else copy b 
min = a if a < b else b 
min = c if c < min else min
max = b if b > a else a
max = c if c > max else max
  
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("The minimum of a,b = ", min) 
print("The maximum of a,b = ", max) 
