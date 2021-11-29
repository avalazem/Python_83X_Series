# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:36:41 2020

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

#Randomly set the score
begin, end, pasfal=50, 100, 70
score = r.randint(begin,end)
  
#Use the ternary operator to determine pass or fail
#grade = "pass" if score >= pasfal else "fail"
#grade="not determined at this point"
if score>=pasfal:
    grade="pass"
if score<pasfal:
    grade="fail"
  
#Print the relevant information
print("With a score of",score,"you",grade,"the course!")