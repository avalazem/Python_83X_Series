# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:26:26 2021

@author: mlehr

Purpose:  Retirement Function
"""

#Future Value Function
def retirement(p,i,n,d):
    f=p
    for y in range(0,n):
        f*=(1+i)
        f+=d
    return f

#Declare initialize Varaibles
pv=0         # $0
intRate=0.05 # 5 percent
numCmpd=48   #48 years
fv=pv        #Set future value = present value at the beginning
deposit=10000 #Deposit into IRA using Municiple Bonds

for year in range(0,numCmpd):
    #fv=fv*(1+intRate)
    fv*=(1+intRate)
    fv+=deposit
    
print("Retirement without a Function(",pv,",",intRate,",",numCmpd,",",deposit,") = $","%6.2f" % fv)

#Now test function 1 to see if it gives the same result
future_value=retirement(pv,intRate,numCmpd,deposit)
print("Retirement without a Function(",pv,",",intRate,",",numCmpd,",",deposit,") = $","%6.2f" % future_value)