# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:26:26 2021

@author: mlehr

Purpose:  Future Value Calculation
"""
import math

#Future Value Function
def savings1(p,i,n):
    f=p
    for y in range(0,n):
        f*=(1+i)
    return f

def savings2(p,i,n):
    return p*(1+i)**n

def savings3(p,i,n):
    if n<=0:
        return p
    return savings3(p,i,n-1)*(1+i)

def savings4(p,i,n):
    return p*math.exp(n*math.log(1+i))

#Declare initialize Varaibles
pv=100       # $100
intRate=0.06 # 6 percent
numCmpd=12   #12 years
fv=pv        #Set future value = present value at the beginning

for year in range(0,numCmpd):
    #fv=fv*(1+intRate)
    fv*=(1+intRate)
    
print("Savings without a Function(",pv,",",intRate,",",numCmpd,") = $","%6.2f" % fv)

#Now test function 1 to see if it gives the same result
future_value1=savings1(pv,intRate,numCmpd)
print("Savings using a for-loop  (",pv,",",intRate,",",numCmpd,") = $","%6.2f" % future_value1)

#Now test function 2 to see if it gives the same result
future_value2=savings2(pv,intRate,numCmpd)
print("Savings using the power   (",pv,",",intRate,",",numCmpd,") = $","%6.2f" % future_value2)

#Now test function 2 to see if it gives the same result
future_value3=savings3(pv,intRate,numCmpd)
print("Savings using a Recursion (",pv,",",intRate,",",numCmpd,") = $","%6.2f" % future_value3)

#Now test function 2 to see if it gives the same result
future_value4=savings4(pv,intRate,numCmpd)
print("Savings using exp and log (",pv,",",intRate,",",numCmpd,") = $","%6.2f" % future_value4)
