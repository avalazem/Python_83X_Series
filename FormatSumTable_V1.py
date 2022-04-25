# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:48:05 2022

@author: mlehr
"""
print("Create a Sum Table about these Center Points")
strtRow=int(input("Input Row Center Point\n"))
strtCol=int(input("Input Column Center Point\n"))
print()

col1=strtCol-1
col2=strtCol-0
col3=strtCol+1

row1=strtRow-1
row2=strtRow-0
row3=strtRow+1


add11=row1+col1
add12=row1+col2
add13=row1+col3
add21=row2+col1
add22=row2+col2
add23=row2+col3
add31=row3+col1
add32=row3+col2
add33=row3+col3

tabHead="{:^45}"
rowHead="{:^10}"
addFmt="{:>6.1f}{:>6.1f}{:>6.1f}"
colFmt="{:>6}{:>6}{:>6}"

print(tabHead.format("Sum Table"))
print()
print(rowHead.format(""),colFmt.format(col1,col2,col3))
print()
print(rowHead.format(row1),addFmt.format(add11,add12,add13))
print(rowHead.format(row2),addFmt.format(add21,add22,add23))
print(rowHead.format(row3),addFmt.format(add31,add32,add33))