"""
    Name:     Dr. Mark E. Lehr
    Date:     September 23rd, 2020
    Purpose:  Set Diagram Exercise
    Versions: First and Last
    
"""

#Fill lists to perform set operations
sSpace=[x for x in range(1,11)]
a=[x for x in range(3,7)]
b=[x for x in range(5,9)]
print("Sample Space = ",sSpace)
print("Set a        =       ",a)
print("Set b        =             ",b,"\n")

setS=set(sSpace)
setA=set(a)
setB=set(b)
print("Sample Space = ",setS)
print("Set a        =       ",setA)
print("Set b        =             ",setB,"\n")

AuB = setA | setB
print("The Union of setA with setB",AuB)

AintrsctB = setA & setB
print("The Intersection of setA with setB",AintrsctB)

Acomp = setS - setA
print("The complement of A",Acomp)

Bcomp = setS - setB
print("The complement of B",Bcomp)

AnotB = setA - setB
print("Set A without set B",AnotB)

BnotA = setB - setA
print("Set B without set A",BnotA)

AuBcomp = setS - AuB
print("The complement of setA union SetB",AuBcomp)