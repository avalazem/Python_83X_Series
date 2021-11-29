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
lstSize=10
lstMnMx=[r.randint(1,100) for x in range(0,lstSize)]
  
# Copy value of a in min if a < b else copy b 
min=max=lstMnMx[0]
for x in lstMnMx:
    min = x if x < min else min
    max = x if x > max else max

print(lstMnMx)
print("The minimum of list = ", min) 
print("The maximum of list = ", max) 