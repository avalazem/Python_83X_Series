# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:18:59 2022

@author: mlehr
"""

list1 = [x    for x in range(1,10,1)   ]
print(list1)

list2 = [2*x    for x in list1]
print(list2)

list3 = [x**2    for x in list1 if x%2==1]
print(list3)