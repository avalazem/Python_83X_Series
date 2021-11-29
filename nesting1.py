# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:00:15 2021

@author: mlehr
"""

set1={1,2,3}
list1=[3,4,5]
tup1=(6,7,8)
obj1={"1":1,"2":2,"3":3}

list2=[set1,list1,tup1,obj1]
list3=[list1,tup1,obj1,set1]

print(list2)
print(list3)

obj2={"List2":list2,"List3":list3}

print(obj2)

refList2=obj2["List2"]
refObj1=obj2["List2"][3]
refElem3Obj1=obj2["List2"][3]["3"]

print(refList2)
print(refObj1)
print(refElem3Obj1)

refObj1["3"]=4

print(refObj1)
print(obj2)

copyList2=list(obj2["List2"])
copyList2[1][1]=8
print(copyList2)
print(list2)