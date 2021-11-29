# -*- coding: utf-8 -*-
"""
Created on Tue Sept 23 15:10:44 202

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

#Declare and initialize variables
score=r.randint(50,100)

#Use Ternary operator to Grade the score
grade = "A" if score>=90 else \
        "B" if score>=80 else \
        "C" if score>=70 else \
        "D" if score>=60 else "F"
        
#Display the Grade
print("Your score of",score,"is a",grade)

print("This is on one line\n",\
      "This is on the next line",\
     )