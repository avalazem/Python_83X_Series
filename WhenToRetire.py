# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:58:53 2021
@author: mlehr
"""
#Initial Conditions
salary=120000      #Salary to retire on
strtBal=0          #Starting Balance
depPerc=0.10       #Regular Deposit percentage of Salary
dep=salary*depPerc #Deposit in $'s
nYears=50          #Number of Compounding Periods
intRate=0.05       #Interest/Investment Rate
savWInt=strtBal    #Savings with interest
retSavReq=salary/intRate  #Required Savings to Retire

#Loop for the number of months you are saving
for years in range(1,nYears+1):
    interest=savWInt*intRate
    savWInt+=(dep+interest)
    
savRslt=strtBal*(1+intRate)**nYears+dep*(1-(1+intRate)**nYears)/(1-(1+intRate))
    
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