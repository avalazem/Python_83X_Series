# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:29:59 2022

@author: mlehr

Purpose:  Simple Conversion from Bitcoin to Dollars
"""

#What is the Constant of conversion form Bitcoin to Dollars
CNVBCDOLS=40769

#Declare and initialize the number of Bitcoin in your wallet
nBitcoin=float(input("Input the Number of Bitcoin to Convert\n"))

#Calculate the number of dollars represented by the 
#number of Bitcoin
nDollars=nBitcoin*CNVBCDOLS

#Display the result
print(nBitcoin,"Bitcoin = $",nDollars)
print(type(CNVBCDOLS))
print(type(nBitcoin))
print(type(nDollars))