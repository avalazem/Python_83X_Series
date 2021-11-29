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
"""

#Importing Numpy for 1 and 2 Dimensional Arrays
import numpy as np
import math

#Finding the pth root of k  k**(1/p)
p=6 #pth root should be 2 or greater and should be an integer
k=10 #classically 2 or greater

#Initialize the 1 and 2 Dimensional Arrays for Recursion
B = np.ones((p,p))
a = np.ones((p,1))
tol=1e-8  #Let the desired accuracey control the number of recursions

#Form B with the Polynomial in k
for row in range(0,p):
    for col in range(row+1,p):
        B[row][col]=k
        
#Display the form of the 1 and 2 Dimensional Arrays
print(B)
print(a)

#Recursive Loop ending with tolerance reached 
anext=0
while math.fabs(a[p-2]/a[p-1]-anext)>tol:
    anext=a[p-2]/a[p-1]
    a=np.matmul(B,a)
    
print("Power operator solution = ", k,"**(1/",p,") = ",k**(1/p))
print("The ratio resultant array")
print(a)
print("Matrix Approximation of the ratios")
for x in range(1,p):
    print(a[x-1]/a[x])