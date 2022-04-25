# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:14:40 2022

@author: mlehr
"""

#List Comprehensions
list1=[x for x in range(1,11)]
list2=[x**2 for x in range(1,11)]
list3=[x**3 for x in range(1,11)]
print(list1)
print(list2)
print(list3)

#Print the output in a table
strFrmt="{:>10}{:>10}{:>10}"
print(strFrmt.format("X","X^2","X^3"))
for x in range(10):
    print(strFrmt.format(list1[x],list2[x],list3[x]))