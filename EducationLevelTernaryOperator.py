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
print("This program determines your level of education")
yrsEduc8 = int(input("Input the number of years in college\n"))
  
# Ternary
grade = "Education Level = "
grade+='K-12' if yrsEduc8 <= 0 else \
       'Under Graduate' if yrsEduc8 <= 4 else \
       'Graduate' if yrsEduc8 <= 6 else \
       'Doctorate' if yrsEduc8 <= 8 else "Post-Doc"

#Print the result
print()
print(grade)