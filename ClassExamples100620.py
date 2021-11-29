"""
Author:  Dr. Mark E. Lehr
Date:    Oct 6th, 2020
Purpose: Scratchpad for-loop, comprehensions, etc....
"""

list1=list(range(1,11))#List constructor with range
print(list1)

list2=[x for x in list1]#List comprehension copy
print(list2)

list3=list(list1)#List constructor with list copy
print(list3)

list4=[x for x in range(1,11)]#List comprehension with range
print(list4)

for indx in range(0,len(list4)):#for loop indx print
    print(list4[indx],"",end="")
print()

list5=[x for x in range(1,11,1)]#List comprehension with range
print(list5)

list6=[]
for x in range(1,11):#List creation by appending
    list6.append(x)
print(list6)

list7=[]
for x in list1:#List copy with appending
    list7.append(x)
print(list7)

print(list1[::])#Indexing implicit

print(list1[::1])#Indexing step explicit

print(list1[::-1])#Reverse the list

list8=list1[2:6]#List creation of [2,3,4,5] index of list 1
print(list8)

list9=list1[2:6:1]#Same just explicit step
print(list9)

for x in list1[2:6]:#Print elements indexed [2,3,4,5]
    print(x,"",end="")
print()

list10=[x for x in range(1,101,6)]#[1,7,13,...]
print(list10)