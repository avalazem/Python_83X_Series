# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:58:53 2021
@author: mlehr
"""

#Include the libraries required
import math

#Initial Conditions
salary=120000      #Salary to retire on
strtBal=0          #Starting Balance
depPerc=0.20       #Regular Deposit percentage of Salary
dep=salary*depPerc #Deposit in $'s
nYears=0           #Number of Compounding Periods
intRate=0.05       #Interest/Investment Rate
savWInt=strtBal    #Savings with interest
retSavReq=salary/intRate  #Required Savings to Retire

#Loop for the number of months you are saving
while savWInt < retSavReq:
    nYears+=1
    interest=savWInt*intRate
    savWInt+=(dep+interest)
    
savRslt=strtBal*(1+intRate)**nYears+dep*(1-(1+intRate)**nYears)/(1-(1+intRate))
yrs2Retire=int((math.log(1+depPerc)-math.log(depPerc))/math.log(1+intRate)+1)
    
#Format and Display the Savings Result
txtFmt="{:9.2f}" 
print("Salary                        = $",txtFmt.format(salary))
print("Initial Balance               = $",txtFmt.format(strtBal))
print("Yearly Interest Rate          =  ",txtFmt.format(intRate*100),"%")
print("Yearly Deposit                = $",txtFmt.format(dep))
print("Number of Years               =  ",txtFmt.format(nYears))
print("Savings with Interest Loop    = $",txtFmt.format(savWInt))
print("Savings with Interest Formula = $",txtFmt.format(savRslt))
print("Required Savings to Retire    = $",txtFmt.format(retSavReq))
print("Calculate years to retire     =  ",txtFmt.format(yrs2Retire))