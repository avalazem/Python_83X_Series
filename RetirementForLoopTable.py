# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:12:06 2022

@author: mlehr
"""

#Initialize the Savings Table
balance=0   #Balance $00
intRate=5   #Percent interest/year
PERCENT=100 #Conversion to decimal representation of %
strtYr=0    #Starting Year
strtD8=2025 #Date to Start Computations
numCmPds=50 #Number of Compounding Periods
salary=100000#Salary of 100000
prcRetire=15 #Percentage to save for Retirement
titlfmt="{:^55}"
balfmt="            ${:>12.2f}{:<20}"
prcfmt="             {:>11.2f}%{:<20}"
colfmt="{:>12}{:>12}{:>12}{:>12}{:>12}"
strfmt="{:12}{:12}{:12.2f}{:12.2f}{:12.2f}"

#Computations
intRate/=PERCENT
prcRetire/=PERCENT
yrlyDep=salary*prcRetire#Yearly Deposit
savReqd=salary/intRate#Savings Required

print(titlfmt.format("Retirement Table"))
print()
print(balfmt.format(balance," = Intital Balance $'s"))
print(prcfmt.format(intRate*PERCENT," = Interest Rate %"))
print(balfmt.format(salary," = Salary $'s/yr"))
print(prcfmt.format(prcRetire*PERCENT," = Salary % Yrly Deposit"))
print(balfmt.format(yrlyDep," = Yearly Deposit $'s/yr"))
print(balfmt.format(savReqd," = Savings required for Retirement"))
print()
print(colfmt.format("Year","Date","Balance","Interest","Yearly"))
print(colfmt.format("","","Beg of Yr","End of Yr","Deposit"))
print()
for year in range(strtYr,numCmPds+1):
    interest=balance*intRate
    print(strfmt.format(year,strtD8+year,balance,interest,yrlyDep))
    balance+=interest
    balance+=yrlyDep