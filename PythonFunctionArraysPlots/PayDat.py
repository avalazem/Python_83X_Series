# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:33:35 2021

@author: mlehr
"""

#Initialize Variables and Declare the data types
strtPay=0.01
multPay=2
nDays=30
sumLst=[]

#Fill the lists
multLst=[multPay**x for x in range(0,nDays)]
payLst=[strtPay*x for x in multLst]
sum=0

#For each pay day accumulate the sum
for x in payLst:
    sum+=x;
    sumLst.append(sum)
    
#Display the Results
#Print the Lists
print("Factor of",multPay,"progression -> ",multLst)
print("Pay per day ->",payLst)
print("Sum per day ->",sumLst)

#Output the Final Check
print("\nYour Final Paycheck =$",sumLst[nDays-1])