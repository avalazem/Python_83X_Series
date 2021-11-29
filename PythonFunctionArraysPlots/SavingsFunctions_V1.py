# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:44:59 2020

@author: Dr. Mark E. Lehr

Purpose:  To illustrate Savings and Retirement Functions
"""

import math

def savings1(p,i,n):
    return p*(1+i)**n

def savings2(p,i,n):
    for n in range(0,n):
        p*=(1+i)
    return p

def savings3(p,i,n):
    return p*math.exp(n*math.log(1+i))

def savings4(p,i,n):
    if n<=0:return p
    return savings4(p,i,n-1)*(1+i)

def retire1(p,i,n,d):
    return p*(1+i)**n+d/i*(1+i)**n-d/i

def retire2(p,i,n,d):
    return savings4(p+d/i,i,n)-d/i

def retire3(p,i,n,d):
    if n==0:return p
    return retire3(p,i,n-1,d)*(1+i)+d

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