"""
    Name:     Dr. Mark E. Lehr
    Date:     September 23rd, 2021
    Purpose:  Boolean Table for just 1 operator Bitwise & 
    Versions: First and Last
    
"""

#Simple Information Heading
print("\nThis Program displays Logical Operator Truth Table")
print("The output is only true when both Boolean Statments are True\n")

#Truth Table Heading
print("  p\t\t  q\t\t  p&q\t p|q\t ~p")

#First Row
p=True
q=True
print(p,"\t",q,"\t",p&q,"\t",p|q,"\t",~p) #Note the p&q Bitwise & operator

#Second Row
p=True
q=False
print(p,"\t",q,"\t",p&q,"\t",p|q,"\t",~p) #Note the p&q Bitwise & operator

#Third Row
p=False
q=True
print(p,"\t",q,"\t",p&q,"\t",p|q,"\t",~p) #Note the p&q Bitwise & operator

#Fourth Row
p=False
q=False
print(p,"\t",q,"\t",p&q,"\t",p|q,"\t",~p) #Note the p&q Bitwise & operator

print()
#Heading
print()
print("This table show the Relational Operator Table")
print("  a\t  b\t  a==b\t  a!=b\t  a<b\t  a<=b\t  a>b\t  a>=b\t ")

#First Row
a=3
b=4
print(" ",a," ",b," ",a==b," ",a!=b)

#Second Row
a=4
b=4
print(" ",a," ",b," ",a==b," ",a!=b)