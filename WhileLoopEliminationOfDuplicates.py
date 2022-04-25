# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:29:45 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

#Randomly set 3 varaibles
begin=1
end=3
a, b, c = r.randint(begin,end), r.randint(begin,end), r.randint(begin,end)
  
#Print the relevant information
print("Possible Duplicates")
print("a = ",a)
print("b = ",b)
print("c = ",c)
print()

#How to make sure there are no duplicates
a, b, c = r.randint(begin,end), r.randint(begin,end), r.randint(begin,end)
while a==b:
    b=r.randint(begin,end)
    
while c==a or c==b:
    c=r.randint(begin,end)
    
#Print the relevant information
print("No possible duplicates")
print("a = ",a)
print("b = ",b)
print("c = ",c)