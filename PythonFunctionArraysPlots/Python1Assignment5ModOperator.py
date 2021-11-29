"""
    Name:     Mark
    Date:     September 23, 2021
    Purpose:  Mod Operator
    Versions: First and Last
    
"""

#Initialize Values
x=int(1234)
print("The original value to dissect = ",x);

#Calculate the 1000's
n1000s=x//1000

#Calculate the 100's
x=x%1000
n100s=x//100 

#Calculate the 10's
x=x%100
n10s=x//10 

#Calculate the 10's
x=x%10
n1s=x

#Print the Results
print("The number of 1000's = ",n1000s)
print("The number of 100's  = ",n100s)
print("The number of 10's   = ",n10s)
print("The number of 1's    = ",n1s)

#Initilize
pennies=int(1234506)
dollars=pennies//100
cents=pennies%100
extra0='0' if cents<10 else ''


#Display the Dollars and Pennies
print()
print("Display pennies in dollar $ format")
print(pennies,' pennies = ',sep="",end="")
print("$",dollars,sep="",end="")
print(".",end="")
print(extra0,end="")
print(cents,sep="",end="")