# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:44:59 2020

@author: Dr. Mark E. Lehr

Purpose:  To illustrate Savings and Retirement Functions
"""

from SavingsAndRetirementFunctionLibrary import *

def main():
    #Initialize variables for the savings/retirement function
    #tests defined above
    PERCENT=100      #Conversion percent = 100
    presVal=100      #Present Value in Savings of $100
    intRate=6.0/100  #Interest Rate in Decimal per year
    numCmpd=12       #Number of compounding periods 12 years
    deposit=100      #Regular Deposit $100 per period
    
    #Display the output for each function
    print("Savings 1 = $%.2f" %savings1(presVal,intRate,numCmpd))
    print("Savings 2 = $%.2f" %savings2(presVal,intRate,numCmpd))
    print("Savings 3 = $%.2f" %savings3(presVal,intRate,numCmpd))
    print("Savings 4 = $%.2f" %savings4(presVal,intRate,numCmpd))
    
    print("Retirement Savings 1 = $%.2f" \
          %retire1(presVal,intRate,numCmpd,deposit))
    print("Retirement Savings 2 = $%.2f" \
          %retire2(presVal,intRate,numCmpd,deposit))
    print("Retirement Savings 3 = $%.2f" \
          %retire3(presVal,intRate,numCmpd,deposit))
    
main()