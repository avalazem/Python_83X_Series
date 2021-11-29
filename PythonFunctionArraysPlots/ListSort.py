"""
    Name:     Mark
    Date:     January 20th, 2021
    Purpose:  List Sort
    Versions: First and Last
    
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Demonstrate a List
a, b, c = r.randint(0,3), r.randint(0,3), r.randint(0,3)
abcList=[a,b,c]
  
#Sort the list
abcList.sort()
  
#Output the result
print(abcList)