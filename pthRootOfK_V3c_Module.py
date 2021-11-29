"""
Author:  Dr. Mark E. Lehr
Data:    November 21st, 2021
Purpose: Multiple Recursion
         1-Dimensional Arrays
         2-Dimensional Arrays
         Numpy Matrix Multiplication
         From November 2021 College Mathematics Journal
         Variables correspond to article
         v2 -> While loop with tolerance and Abs Value with math library
         v3 -> Creating a function to return the result
         v3a -> Creating another function to return the result
         v3b -> Putting functions in Modules
         v3c -> Importing only elements you need from the module
"""

#Importing pthRoot Module
from pthRootModule import pthRoot

#Finding the pth root of k  k**(1/p)
p=int(6)  #pth root should be 2 or greater and should be an integer
k=10      #classically 2 or greater
tol=1e-6  #Let the desired accuracey control the number of recursions

#Compare Results
print("Power operator solution = ", k,"**(1/",p,") = ",k**(1/p))
print("The ratio resultant     =", pthRoot(p,k,tol))