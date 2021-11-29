"""
Author:  Dr. Mark E. Lehr
Data:    November 21st, 2021
Purpose: Multiple Recursion
         1-Dimensional Arrays
         2-Dimensional Arrays
         Numpy Matrix Multiplication
         From November 2021 College Mathematics Journal
"""

#Importing Numpy for 1 and 2 Dimensional Arrays
import numpy as np

#Finding the pth root of k  k**(1/p)
p=2
k=2

#Initialize the 1 and 2 Dimensional Arrays for Recursion
B = np.ones((p,p))
a = np.ones((p,1))
nLoops=1

#Form B with the Polynomial in k
for row in range(0,root):
    for col in range(row+1,root):
        B[row][col]=k

#
for 
        

for count in range(0,n):
    a=np.matmul(B,a)
    print("Matrix Approximation")
    print(a[root-2]/a[root-1])