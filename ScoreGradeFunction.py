# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:40:35 2022

@author: mlehr
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Your Code Here!
def gradeTerOp(score):
    
    grade="A" if(score>=90) else \
          "B" if(score>=80) else \
          "C" if(score>=70) else \
          "D" if(score>=60) else"F"
        
    return grade

def gradeDepIf(score):
    
    if(score>=90):  grade="A"
    elif(score>=80):grade="B"
    elif(score>=70):grade="C"
    elif(score>=60):grade="D"
    else:           grade="F"
        
    return grade

def gradeInDepIf(score):
    
    if(score>=90):             grade="A"
    if(score>=80 and score<90):grade="B"
    if(score>=70 and score<80):grade="C"
    if(score>=60 and score<70):grade="D"
    if(score<60):              grade="F"
        
    return grade

def main():
    scrLst = [r.randint(50,100) for x in range(0,10)]
    for score in scrLst:
        print("Score = ",score,"Grade = ",gradeDepIf(score))
        print("Score = ",score,"Grade = ",gradeInDepIf(score))
        print("Score = ",score,"Grade = ",gradeTerOp(score))
        print()

main()