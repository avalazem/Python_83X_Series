"""
 * File:   main.cpp
 * Author: Dr. Mark E. Lehr
 * Created on April 24th, 2022, 11:32 AM
 * Purpose:  Flowchart Exercise of each construct
"""

#Declare and Initialize Variables
x=int(input("Input the value of x, x must be integer >= 0 and <= 2\n"))
msg=""

#Branching Construct Independent - If
if(x<0): print("Value too Small")
if(x>2): print("Value too Large")
if(x>=0 and x<=2):print("In Range [0,2]")

#Branching Construct Dependent If - else if
if(x<0):   print("Value too Small")
elif(x>2): print("Value too Large")
else:      print("In Range [0,2]")
 
#Branching Ternary Operator which are really good at returning 1
#value and must be of the same type
msg += "Value too Small\n" if x<0 else \
      "Value too Large\n" if x>2 else \
      "In Range [0,2]\n"
print(msg)

#Looping Construct for-loop
floop=5;
for i in range(1,floop+1):
    print(i," ",end="")
print()

#Looping Construct while-loop
wloop=5
j=1
while(j<=wloop):
    print(j," ",end="")
    j+=1
print()