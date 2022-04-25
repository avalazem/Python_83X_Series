# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:32:32 2022

@author: mlehr
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:19:04 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

# Program to demonstrate conditional operator 
score = r.randint(50,100)
  
# Copy value of a in min if a < b else copy b 
grade='A' if score >= 90 else \
      'B' if score >= 80 else \
      'C' if score >= 70 else \
      'D' if score >= 60 else 'F'

#Print the result
print("Score of",score,"=",grade)