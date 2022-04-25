# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 18:15:12 2022

@author: mlehr
"""

#Initialize the Savings Table
balance=100 #Balance $100
intRate=6   #Percent interest/year
PERCENT=100 #Conversion to decimal representation of %
strtYr=0    #Starting Year
strtD8=2022 #Date to Start Computations
numCmPds=12 #Number of Compounding Periods
titlfmt="{:^55}"
balfmt="            ${:>6.2f}{:<20}"
prcfmt="             {:>5.2f}%{:<20}"
colfmt="{:>10}{:>10}{:>10}{:>10}"
strfmt="{:10}{:10}{:10.2f}{:10.2f}"

#Computations
intRate/=PERCENT
print(titlfmt.format("Savings Table"))
print()
print(balfmt.format(balance," = Intital Balance $'s"))
print(prcfmt.format(intRate*PERCENT," = Interest Rate %"))
print()
print(colfmt.format("Year","Date","Balance","Interest"))
print(colfmt.format("","","Beg of Yr","End of Yr"))
print()
for year in range(strtYr,numCmPds+1):
    interest=balance*intRate
    print(strfmt.format(year,strtD8+year,balance,interest))
    balance+=interest