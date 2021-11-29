# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:58:53 2021
@author: mlehr
"""
#Initial Conditions
strtBal=100        #Starting Balance
dep=100            #Deposit in $'s
nMonths=144        #Number of Compounding Periods
intRate=0.06/12    #Interest/Investment Rate
savWInt=strtBal    #Savings with interest
savWOInt=strtBal   #Savings without interest

#Loop for the number of months you are saving
for months in range(1,nMonths+1):
    interest=savWInt*intRate
    savWInt+=(dep+interest)
    savWOInt+=dep
    
savRslt=strtBal*(1+intRate)**nMonths+dep*(1-(1+intRate)**nMonths)/(1-(1+intRate))
    
#Format and Display the Savings Result
txtFmt="{:9.2f}" 
diff=savWInt-savWOInt
print("Initial Balance               = $",txtFmt.format(strtBal))
print("Yearly Interest Rate          =  ",txtFmt.format(intRate*1200),"%")
print("APR                           =  ",txtFmt.format(((1+intRate)**12-1)*100),"%")
print("Monthly Deposit               = $",txtFmt.format(dep))
print("Number of Months              =  ",txtFmt.format(nMonths))
print("Number of Years               =  ",txtFmt.format(nMonths/12))
print("Savings with Interest Loop    = $",txtFmt.format(savWInt))
print("Savings with Interest Formula = $",txtFmt.format(savRslt))
print("Savings with out Interest     = $",txtFmt.format(savWOInt))
print("The difference with interest  = $",txtFmt.format(diff))
    