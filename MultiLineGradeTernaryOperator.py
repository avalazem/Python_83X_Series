"""
    Name:     Mark
    Date:     March 15th, 2022
    Purpose:  Ternary Operator and Relational Operators
    Versions: Grading a Score
    
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
score=r.randint(50,100)
grade="A" if score>=90 else \
      "B" if score>=80 else \
      "C" if score>=70 else \
      "D" if score>=60 else "F"

print(score," = ",grade)