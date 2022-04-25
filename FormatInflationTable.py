# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:58:14 2022

@author: mlehr
"""

#Initialize the Savings Table
price=0.19 #Balance $100
infRate=6   #Percent inflation/year
PERCENT=100 #Conversion to decimal representation of %
strtYr=0    #Starting Year
strtD8=1962 #Date to Start Computations
numCmPds=60 #Number of Compounding Periods
titlfmt="{:^55}"
balfmt="            ${:>6.2f}{:<20}"
prcfmt="             {:>5.2f}%{:<20}"
colfmt="{:>10}{:>10}{:>10}{:>10}"
strfmt="{:10}{:10}{:10.2f}{:10.2f}"

#Computations
infRate/=PERCENT
print(titlfmt.format("Inflation Table"))
print()
print(balfmt.format(price," = Intital Price $'s"))
print(prcfmt.format(infRate*PERCENT," = Inflation Rate %"))
print()
print(colfmt.format("Year","Date","Price","Inflation"))
print(colfmt.format("","","Beg of Yr","End of Yr"))
print()
for year in range(strtYr,numCmPds+1):
    inflation=price*infRate
    print(strfmt.format(year,strtD8+year,price,inflation))
    price+=inflation