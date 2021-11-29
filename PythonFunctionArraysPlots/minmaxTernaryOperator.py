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
a, b = r.randint(0,1), r.randint(0,1)
  
# Copy value of a in min if a < b else copy b 
min = a if a < b else b 
max = b if b > a else a
  
print("a = ",a)
print("b = ",b)
print("The minimum of a,b = ", min) 
print("The maximum of a,b = ", max) 

