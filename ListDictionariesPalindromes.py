# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:17:10 2022

@author: mlehr
"""

key=["A","B","C","D","E"]
values=["a","b","c","d","e"]
mapLetrs={}
mapLetrs[key[0]]=values[0]
mapLetrs[key[1]]=values[1]
mapLetrs[key[2]]=values[2]
mapLetrs[key[3]]=values[3]
mapLetrs[key[4]]=values[4]
print(mapLetrs)

mapLetrs={key[i]:values[i] for i in range(len(key))}
print(mapLetrs)

mapLetrs={key[i]:values[i] for i in range(len(values))}
print(mapLetrs)

letters=["A","B","C","D","E","A","B","C","D","E"]
print(letters)
ltrSet=set(letters)
print(ltrSet)
mode=False if len(letters)!=len(ltrSet) else True
print("List letters is mode either True or False = ",mode)

name="hannah"

print(name, " -> Palindrome -> ",end="")
print(True) if name==name[::-1] else print(False)