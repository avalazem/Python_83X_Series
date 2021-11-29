"""
    Name:     Mark
    Date:     July 20th, 2021
    Purpose:  To Sort a List
    Versions: First and Last
    
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate a List Sort
a, b, c = r.randint(0,3), r.randint(0,3), r.randint(0,3)
abcList = [a,b,c]  
print("The List before Sorting",abcList)

# Sort the list
abcList.sort()
min = abcList[0]
max = abcList[2]
mid = abcList[1]
  
print("The List after Sorting ",abcList)
print("The minimum of a,b,c = ", min) 
print("The middle  of a,b,c = ", mid) 
print("The maximum of a,b,c = ", max) 