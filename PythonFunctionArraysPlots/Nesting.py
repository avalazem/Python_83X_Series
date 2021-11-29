# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:12:12 2021

@author: mlehr
"""

obj1={"1":1,"11":11,"111":111}
obj2={"2":2,"22":22,"222":222}
obj3={"3":3,"33":33,"333":333}

list1=[obj1,obj2,obj3]
list2=[1,2,3]
list3=[4,5,6]

obj00={"Object":{"This":1,"That":2,"ortheOther":3}}
obj11={"list1":list1,"list2":list2,"list3":list3}

grandObj={"obj00":obj00,"obj11":obj11}
print(grandObj)
`
print(grandObj["obj11"]["list3"][1])

copyList3a=[x for x in grandObj["obj11"]["list3"]]
copyList3b=list(grandObj["obj11"]["list3"])
refList3c=grandObj["obj11"]["list3"]
print(copyList3a)
print(copyList3b)
print(refList3c)

refList3c[1]=666

print(grandObj)