# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:41:14 2022

@author: mlehr
"""

#Initialize Data for the Savings/Inflation Calculator
balPrice=100#$100
invInfRate=0.06#6 per cent/year

#Format String
strFrmt="{:^10}{:^10}{:^10}{:^10}"
numFrmt="{:>5}     {:^10}{:^10.2f}{:^10.2f}"
print(strFrmt.format("","","Savings/Inflation Calculator",""))
print()
print(strFrmt.format("",balPrice,"= Balance or Item Price",""))
print(strFrmt.format("",invInfRate,"= Investement or Inflation",""))
print()
print(strFrmt.format("","","Price or","Inflation or"))
print(strFrmt.format("Year","Date","Balance","Interest"))

#for-Loop the table
nYears=12
date=2022
for year in range(nYears+1):
    intInf8shn=balPrice*invInfRate
    print(numFrmt.format(year,date+year,balPrice,intInf8shn))
    balPrice+=intInf8shn
    