# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:35:19 2022

@author: mlehr
"""

#Include the math library
import math

#Input the x for exp(x)
strFmt="{:10.7f}"
x=float(input("Input the x for exp(x)\n"))
nTerms=int(input("Input the number terms used in Approximation\n"))
print("e ^",x," = ",strFmt.format(math.exp(x)))
tol=1e-8

#Approximate the exp(x) with the number of terms in series
apprxExp=1
termVal=1
for i in range(1,nTerms+1):
    termVal*=x/i
    apprxExp+=termVal
    if termVal<tol:
        break
    
#Output the approximation results
print("e ^",x," = ",strFmt.format(apprxExp)," <- approximate value")
print("Number of terms used = ",i)