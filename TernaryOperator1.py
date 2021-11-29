"""
Created on Thu Oct  14 19:23:54 2020

@author: Dr. Mark E. Lehr

Purpose:  To illustrate the 3 ways to us if's'

"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

# Set the score with a random number
lowScr=50
highScr=100
score = r.randint(lowScr,highScr)
  
# Determine the grade with a ternary operator and the line continuation
grade = "A" if score >= 90 else \
        "B" if score >= 80 else \
        "C" if score >= 70 else \
        "D" if score >= 60 else "F"

print("Your score =", score,"giving you a grade of ",grade)