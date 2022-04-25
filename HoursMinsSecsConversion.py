# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:10:32 2022

@author: mlehr
"""

#Convert years to seconds
CNVYRDYS=365
CNVDYSHRS=24
CNVHRSMIN=60
CNVMINSECS=60

#Input number of years
strYears=input("Input Number of Years to Convert to Seconds\n")
years=float(strYears)

#Equate years to seconds
seconds = years * CNVYRDYS * CNVDYSHRS * CNVHRSMIN * CNVMINSECS

#Display the results
strFormat="\n{:.2f} years = {:.4e} seconds"
print(strFormat.format(years,seconds))