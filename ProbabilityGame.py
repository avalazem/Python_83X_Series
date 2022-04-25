# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:34:26 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

#Fill the list with random numbers
aOut=True
aWorks=1.0/3
bOut=True
bWorks=0.50
cOut=True
cWorks=1.00
  
while aOut+bOut+cOut > 1:
    if(r.uniform(0,1) <= aWorks and aOut):
        if(cOut):cOut=False
        else: bOut=False
    if(r.uniform(0,1) <= bWorks and bOut):
        if(cOut):cOut=False
        else: aOut=False
    if(r.uniform(0,1) <= cWorks and cOut):
        if(bOut):bOut=False
        else: aOut=False
        
if(aOut):print("A wins the cake")
if(bOut):print("B wins the cake")
if(cOut):print("C wins the cake")