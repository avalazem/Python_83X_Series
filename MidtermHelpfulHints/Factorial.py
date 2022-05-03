# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:09:17 2022

@author: mlehr
"""

#Initialize the N in N!
n=int(input("Input n output n!\n"))
if n<=0:
    n=0
fact=1

#Loop to calculate the factorial
for x in range(1,n+1):
    fact*=x
    
#Output the Factorial
print(n,"! = ",fact)