"""
    Name:     Dr. Mark E. Lehr
    Date:     September 23rd, 2021
    Purpose:  Boolean Table for just 1 operator Bitwise & 
    Versions: First and Last
    
"""

#Simple Information Heading
print("\nThis Program displays the Bitwise & Truth Table")
print("The output is only true when both Boolean Statments are True\n")

#Truth Table Heading
print("  p\t\t  q\t\t  p&q")

#First Row
p=True
q=True
print(p,"\t",q,"\t",p&q) #Note the p&q Bitwise & operator

#Second Row
p=True
q=False
print(p,"\t",q,"\t",p&q) #Note the p&q Bitwise & operator

#Third Row
p=False
q=True
print(p,"\t",q,"\t",p&q) #Note the p&q Bitwise & operator

#Fourth Row
p=False
q=True
print(p,"\t",q,"\t",p&q) #Note the p&q Bitwise & operator