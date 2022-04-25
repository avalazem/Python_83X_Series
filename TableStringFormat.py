# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:57:36 2022

@author: mlehr
"""

#Create a Table with factors and *, ^^, /
print("Develop a Table in Accordance with the Assignment")
inValue=int(input("Read in the Table Value.\n"))
row1Fac,row2Fac,row3Fac=map(int,input("Input 3 Factors\n").split())

#Print out Table
heading1="{:30} {:^10}"
heading2="{:<30}{:^10}"
heading3="{:<20}{:^10}{:^10}{:^10}"
allRows="{:^6}{:14}{:^10}{:^10}{:^10}"
print()
print(heading1.format("","Input"))
print(heading2.format("Factor",inValue))
print()
print(heading3.format("","Times","Power","Divide"))
print(allRows.format(row1Fac,"",row1Fac*inValue,inValue**row1Fac,int(inValue/row1Fac)))
print(allRows.format(row2Fac,"",row2Fac*inValue,inValue**row2Fac,int(inValue/row2Fac)))
print(allRows.format(row3Fac,"",row3Fac*inValue,inValue**row3Fac,int(inValue/row3Fac)))