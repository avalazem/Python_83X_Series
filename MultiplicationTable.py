# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:25:07 2021

@author: mlehr
"""

#Initialize Variables and Declare the data types
row=[4,5,6,7]
col=[3,5,7,9]

#Headings for the Multiplication Table
print("Multiplication Table\n")
for c in col:
    print("\t ",c,end="")
print("\n")

#Now fill the table 1 row at a time
for r in row:
    print(r,end="")
    for c in col:
        print("\t",r*c,end="")
    print()