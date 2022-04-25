# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:52:14 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

#Filling a list with a comprehension
myList1=[x for x in range(2,11,2)]
print(myList1)
myList2=[int(r.random()*10+1) for x in range(1,11,2)]
print(myList2)
set1=set(myList2)
print(set1)
mode="This List has a mode" if len(set1)!=len(myList2) else "No Mode"
print(mode)
print()

#A lot of data
index=[x for x in range(1,1001)]
print(index)
print()

#Create a dictionary utilizing comprehensions
key=[x for x in range(1,11)]
value=[x*x for x in key]
print(key)
print(value)

dict1={key[x]:value[x] for x in range(0,len(key))}
print(dict1)
print()

#How to create a 2 D List
list2D=[[1,2,3],[4,5,6],[7,8,9]]
print(list2D)
print(list2D[1][1])
print()

#Trying to utilize a comprehesion for 2D list
listC2D=[[col+row for col in range(1,4)] for row in range(0,7,3)]
print(listC2D)
print(listC2D[1][1])