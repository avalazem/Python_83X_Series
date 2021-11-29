"""
    Name:     Mark
    Date:     January 21st, 2020
    Purpose:  Ternary Operator and Relational Operators
    Versions: First and Last
    
"""

"""
Problem 1)  Sorting Problem

     Input or (set with random) 3 integer data types input1, input2, input3

     Use the Ternary Operator, Logical Operators, Relational operators to sort the 3 inputs like the previous assignment finding min -> minimum and max -> maximum

     Of course, this time you will need to find the mid -> middle.
    
"""
#Import the random number generator and set the seed with time
import random as r
from datetime import datetime as d
r.seed(d.now())

#Randomly choose 2 variables
a = r.randint(1,3)
b = r.randint(1,3)
c = r.randint(1,3)

#Output the random variables
print("The Sorting Problem!")
print("The 3 random variables to sort")
print("a = ",a)
print("b = ",b)
print("c = ",c)

#Determine which is min and max and then in the middle
mn =  a if a <= b and a <= c else \
      b if b <= a and b <= c else c
mx =  a if a >= b and a >= c else \
      b if b >= a and b >= c else c
mid = a if (mn == b or mx == b) and (mn == c or mx == c) and (c!=b) else \
      b if (mn == a or mx == a) and (mn == c or mx == c) and (a!=c) else c

#Output the min and the max
print("The ordered List")
print("max = ",mx)
print("mid = ",mid)
print("min = ",mn)

"""
Problem 2)  Paycheck Problem

     Input the payRate -> $'s/hour,   and hrsWrkd -> hours

     Calculate the payChck with the following conditions

                      Straight time for the first 40 hours

                      Double time for hours above 40 hours
"""

#Input random payRate and Hrswrkd
payRate = r.randint(1,2)*10    #Pay Rate $'s/hr
hrsWrkd = r.randint(3,5)*10    #Hours Worked
OVRTIME = 40                   #Hours were overtime begins

#Calculation for straight time then the overtime hours added
payChk  = payRate * hrsWrkd
payChk += (hrsWrkd - OVRTIME)*payRate if hrsWrkd > OVRTIME else 0

#Output the Paycheck
print()
print("Paycheck Problem")
print("Pay Check = $",payChk,"for",hrsWrkd,"hours @",payRate,"$'s/hr")


"""
Problem 3)  Rental Problem

     Input the rental rate (rntlRate -> $'s/hour),   and hours rented (hrsRntd -> hours)

     Calculate the Rental Cost with the following conditions

     The minimum time is charged as 4 hours, then every hour after is at the rental rate.
"""
#Input random rental rate and hours rented
rntlR8   = r.randint(1,2)*10   #Rental Rate $'s/hr
hrsRntd  = r.randint(1,8)      #Hours Rented
MINTIME  = 4                   #Minimum hours to rent

#Calculation for straight time then the overtime hours added
hrsCrgd = hrsRntd if hrsRntd >= MINTIME else MINTIME
rntlCst = rntlR8 * hrsCrgd

#Output the Paycheck
print()
print("Rental Problem")
print("Rental Cost = $",rntlCst,"for",hrsRntd,"hours @",rntlR8,"$'s/hr")
