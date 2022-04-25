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
hours=r.randint(30,50)
payRate=r.randint(15,25)
ovrTime=40
hours=50
payRate=10

#Calculate the paycheck, double time after Overtime occurs
payChk=hours*payRate
payChk+=(hours-ovrTime)*payRate if hours>ovrTime else 0

print("Pay Check = $",payChk,"for",hours,"hours worked at $",payRate,"/hour")