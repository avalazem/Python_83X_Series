# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:49:54 2021

@author: mlehr
"""
#Inputs for creation of the table
tabStrt=12
row1=2
row2=3
row3=4

#Column 1 of the table
n11=int(row1*tabStrt)
n21=int(row2*tabStrt)
n31=int(row3*tabStrt)

#Column 2 of the table
n12=int(tabStrt**row1)
n22=int(tabStrt**row2)
n32=int(tabStrt**row3)

#Column 3 of the table
n13=int(tabStrt/row1)
n23=int(tabStrt/row2)
n33=int(tabStrt/row3)

#Raw Output Centered fixed 0 decimal places
hd1="{:^30}{:^10}"
print(hd1.format("","Input"))
hd2="{:^10}{:^20}{:^10}"
print(hd2.format("Factor","",tabStrt))
print()
hd3="{:^20}{:^10}{:^10}{:^10}"
print(hd3.format("","Times","Power","Divide"))
txtRow="{:^10}{:^10}{:^10.0f}{:^10.0f}{:^10.0f}"
print(txtRow.format(row1,"",n11,n12,n13))
print(txtRow.format(row2,"",n21,n22,n23))
print(txtRow.format(row3,"",n31,n32,n33))
print()

#Decimal Output Right justified 2 places
print(hd1.format("","Input"))
print(hd2.format("Factor","",tabStrt))
print()
print(hd3.format("","Times","Power","Divide"))
txtRow="{:^10}{:^10}{:>10.2f}{:>10.2f}{:>10.2f}"
print()
print(txtRow.format(row1,"",n11,n12,n13))
print(txtRow.format(row2,"",n21,n22,n23))
print(txtRow.format(row3,"",n31,n32,n33))
print()

#Exponential Output Centered 2 Significant Digits
print(hd1.format("","Input"))
print(hd2.format("Factor","",tabStrt))
print()
print(hd3.format("","Times","Power","Divide"))
txtRow="{:^10}{:^10}{:^10.2e}{:^10.2e}{:^10.2e}"
print()
print(txtRow.format(row1,"",n11,n12,n13))
print(txtRow.format(row2,"",n21,n22,n23))
print(txtRow.format(row3,"",n31,n32,n33))
print()

#Octal Output Left Justified
print(hd1.format("","Input"))
print(hd2.format("Factor","",tabStrt))
print()
print(hd3.format("","Times","Power","Divide"))
txtRow="{:^10}{:^10}{:<10o}{:<10o}{:<10o}"
print()
print(txtRow.format(row1,"",n11,n12,n13))
print(txtRow.format(row2,"",n21,n22,n23))
print(txtRow.format(row3,"",n31,n32,n33))