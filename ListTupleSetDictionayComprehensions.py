# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:34:32 2022

@author: mlehr
"""

#List Comprehension
list1=[x for x in range(3,15,2)]
print(list1)
list2=[x for x in range(3,15)]
print(list2)
list3=[x for x in list2]
print(list3)
list4=[x for x in list2 if x%2==1]
print(list4)
list5=[x for x in list2 if x%2==0]
print(list5)

#Set Comprehension
set1={x for x in range(3,15,2)}
print(set1)
set2={x for x in list1}
print(set2)

#Dictionary Comprehensions
keyList=["Key1","Key2","Key3"]
valList=[1,2,3]
print(keyList)
print(valList)
dict1={keyList[x]:valList[x] for x in range(0,len(keyList))}
print(dict1)

#Tuple Comprehension
tuple1=tuple(x for x in list1)
print(tuple1)
tuple2=tuple(x for x in range(1,11))
print(tuple2)