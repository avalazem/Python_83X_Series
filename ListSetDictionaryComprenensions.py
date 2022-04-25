# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:09:27 2022

@author: mlehr
"""

list1=[x%3 for x in range(1,11)]
set1=set(list1)
noMode="True" if len(list1)==len(set1) else "False"

print(list1)
print(set1)
print("The List has no modes ->",noMode)

dict1={"Key1":"value1","key2":"value2"}
for x in dict1:
    print(x,dict1[x])