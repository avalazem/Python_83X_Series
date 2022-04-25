# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:40:39 2022

@author: mlehr
"""

#Input the number of Bitcoin
strBitcoin = input("How many Bitcoin do you own at Paypal?\n")
nBitcoin   = float(strBitcoin)

#Map the Bitcoin to the Dollar Representation
CVNBITCDLS = 4.447414e4#Conversion to Dollars $44,474.14/Bitcoin
eqvDollars = nBitcoin * CVNBITCDLS

#Output the results
strFormat="\n {:.4f}  bitcoin = $ {:.2f}"
print(strFormat.format(nBitcoin,eqvDollars))

strFormat="\n {:12.3e}  bitcoin = $ {:15.5e}"
print(strFormat.format(nBitcoin,eqvDollars))