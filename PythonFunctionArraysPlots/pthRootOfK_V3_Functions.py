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
"""

#Importing Numpy for 1 and 2 Dimensional Arrays and math
import numpy as np
import math

#Define a couple of functions to perfrom the above task
def pthRoot(p,k,tol):
    #Initialize the matrix and vector
    B = np.ones((p,p))
    a = np.ones((p,1))
    #Form B with the Polynomial in k
    for row in range(0,p):
        for col in range(row+1,p):
            B[row][col]=k
    #Is the result close enough?
    aafter=1
    abefore=0
    while math.fabs(aafter-abefore)>tol:
        abefore=a[p-2]/a[p-1]
        a=np.matmul(B,a)
        aafter=a[p-2]/a[p-1]
    return aafter;

#Finding the pth root of k  k**(1/p)
p=int(6)  #pth root should be 2 or greater and should be an integer
k=10       #classically 2 or greater
tol=1e-8  #Let the desired accuracey control the number of recursions

#Compare Results
print("Power operator solution = ", k,"**(1/",p,") = ",k**(1/p))
print("The ratio resultant     =", pthRoot(p,k,tol))