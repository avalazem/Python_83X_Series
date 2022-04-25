# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:33:33 2022

@author: mlehr
"""

#Input the number Miles Drivin and the Number of Gallons to Fill Vehicle
print("This program solves your vehicles MPG")
strMilesDrvn = input("How many miles did you drive?\n")
milesDrvn    = float(strMilesDrvn)
strNGallons  = input("How many gallons of gas to fill your Vehicle?\n")
nGallons     = float(strNGallons)

#Map the Bitcoin to the Dollar Representation
mpg = milesDrvn/nGallons

#Output the results
strFormat="\n {:.1f} MPG = {:.1f} Miles Drvin / {:.1f} Gallons to Fill"
print(strFormat.format(mpg,milesDrvn,nGallons))