# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:19:04 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
a, b, c = r.randint(0,3), r.randint(0,3), r.randint(0,3)
  
# Copy value of a in min if a < b else copy b 
min = a if ((a <= b)  and (a <= c)) else \
      b if ((b <= c)  and (b <= a)) else c
max = a if ((a >= b)  and (a >= c)) else \
      b if ((b >= a)  and (b >= c)) else c
  
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("The minimum of a,b,c = ", min) 
print("The maximum of a,b,c = ", max) 