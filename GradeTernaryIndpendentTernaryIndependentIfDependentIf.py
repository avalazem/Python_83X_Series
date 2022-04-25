# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:30:17 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
score=r.randint(50,100)

#Dependent Ternary Operator Implementation on 4 Logical but 1 Physical Line
#of code
grade='A' if score >= 90 else \
      'B' if score >= 80 else \
      'C' if score >= 70 else \
      'D' if score >= 60 else 'F'

print("Score of",score,"=",grade)

#Independent Ternary Operator Implementation
grade=''
grade+='A' if score >= 90 else ''
grade+='B' if score >= 80 and score < 90 else ''
grade+='C' if score >= 70 and score < 80 else ''
grade+='D' if score >= 60 and score < 70 else ''
grade+='F' if score <  60 else ''

print("Score of",score,"=",grade)

#Dependent if statement
if   score >= 90:
    grade='A'
elif score >= 80:
    grade='B'
elif score >= 70:
    grade='C'
elif score >= 60:
    grade='D'
else:
    grade='F'

print("Score of",score,"=",grade)

#Indendent if statement
if score >= 90:
    grade='A'
if score >= 80 and score < 90:
    grade='B'
if score >= 70 and score < 80:
    grade='C'
if score >= 60 and score < 70:
    grade='D'  
if score < 60:
    grade='F'

print("Score of",score,"=",grade)