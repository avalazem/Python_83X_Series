# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 04:10:12 2022

@author: mlehr
"""

#import the random number generator and set the seed
print("This program calculates your gross pay in $'s")
hrsWrkd = float(input("Input the number of hours worked in a week\n"))
payRate = float(input("Input your pay rate in $s/hour\n"))
ovrTime = 40

# Copy value of a in min if a < b else copy b
payChk = hrsWrkd * payRate
payChk += (hrsWrkd - ovrTime) * payRate if hrsWrkd > ovrTime else 0

#Print the result
print("\nPay Check = $",payChk)