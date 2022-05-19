# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:27:27 2022

@author: mlehr
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Your Code Here!
def netPay_v3(hours,payRate):
    #Ternary Operator
    paychk=hours*payRate if(hours<=40) else \
           40*payRate+2*payRate*(hours-40)    
    return paychk

def netPay_v2(hours,payRate):
    #Dependent If
    if(hours<=40):paychk=hours*payRate
    else:         paychk=40*payRate+2*payRate*(hours-40)    
    return paychk

def netPay_v1(hours,payRate):
    #Independent If
    paychk=hours*payRate
    if(hours>40):paychk+=(hours-40)*payRate
    return paychk

def main():
    payRate=r.randint(12,25)
    hours=r.randint(30,50)
    print("Hours Worked = ",hours,"Pay Rate = ",payRate)
    print("Net Pay Check = $",netPay_v1(hours,payRate))
    print("Net Pay Check = $",netPay_v2(hours,payRate))
    print("Net Pay Check = $",netPay_v3(hours,payRate))

main()