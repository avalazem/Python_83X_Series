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
grade=""
grade+="A" if score>=90 and score<=100 else ""
grade+="B" if score>=80 and score<90   else ""
grade+="C" if score>=70 and score<80   else ""
grade+="D" if score>=60 and score<70   else ""
grade+="F" if score>=0  and score<60   else ""

print(score," = ",grade)