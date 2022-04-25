# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:49:58 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
hrsWrkd=r.randint(0,80)#Random Hours from 0 to 80
payRate=15#Pay rate = 15
ovrTme1=40#Hours at which Double time applies
ovrTme2=50#Hours at which Triple time applies

#Straight Time
payChk=hrsWrkd*payRate

#Double Time
if hrsWrkd > ovrTme1:
    payChk += (hrsWrkd-ovrTme1)*payRate
    
#Triple time
if hrsWrkd > ovrTme2:
    payChk += (hrsWrkd-ovrTme2)*payRate
    
#Display the paycheck    
print("For",hrsWrkd,"hours worked your Paycheck =$",payChk)