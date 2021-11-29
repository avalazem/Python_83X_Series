# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:38:44 2021

@author: mlehr
"""

#import the random number generator and set the seed
import random as rnd
from datetime import datetime as d
rnd.seed(d.now())

# Program to demonstrate conditional operator 
a, b = rnd.randint(0,21), rnd.randint(0,21)

#Ternary Operator
min=a if a<b else b
max=b if b>a else a

#Display the results of
print("a = ",a)
print("b = ",b)
print("The minimum of a,b = ", min) 
print("The maximum of a,b = ", max)

#Initialize Variables and Declare the data types
#Data
row=[4,5,6,7]
col=[3,5,7,9]


#Print the headings
print("\nMultiplication Table\n")

for c in col:
    print("\t ",c,end="")
print("\n")

#Print each row
for r in row:
    print(r,end="")
    for c in col:
        print("\t",r*c,end="")
    print()
        
#Initialize Pay per day Variables and Declare the data types
strtPay=25
multPay=2
nDays=5
sumLst=[]

#Fill the lists
multLst=[multPay**x for x in range(0,nDays)]
payLst=[strtPay*x for x in multLst]
sum=0

#Loop on x in the list
for x in payLst:
    sum+=x;
    sumLst.append(sum)
    
#Print the Lists
print("Factor of",multPay,"progression -> ",multLst)
print("Pay per day ->",payLst)
print("Sum per day ->",sumLst)

#Output the Final Check
print("\nYour Final Paycheck =$",sumLst[nDays-1])