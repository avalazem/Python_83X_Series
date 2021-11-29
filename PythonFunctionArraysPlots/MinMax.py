# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:52:06 2021

@author: mlehr
"""

#Import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Randomly Set A and B
a, b = r.randint(0,21), r.randint(0,21)

#Determine the min
min=a if a<b else b

#Determine the min
max=b if b>a else a

#Display the output
print("a = ",a)
print("b = ",b)
print("The minimum of a,b = ", min) 
print("The maximum of a,b = ", max)