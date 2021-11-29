"""
Author:  Dr. Mark E. Lehr
Data:    November 21st, 2021
Purpose: Multiple Recursion
         1-Dimensional Arrays
         2-Dimensional Arrays
         Numpy Matrix Multiplication
         From November 2021 College Mathematics Journal
         Variables correspond to article
"""

#Importing Numpy for 1 and 2 Dimensional Arrays
import numpy as np

#Finding the pth root of k  k**(1/p)
p=2
k=2

#Initialize the 1 and 2 Dimensional Arrays for Recursion
B = np.ones((p,p))
a = np.ones((p,1))
nRec=10  #How many recursions

#Form B with the Polynomial in k
for row in range(0,p):
    for col in range(row+1,p):
        B[row][col]=k
        
#Display the form of the 1 and 2 Dimensional Arrays
print(B)
print(a)

#Recursive Loop with Numpy 
for loop in range(0,nRec):
    a=np.matmul(B,a)
    
print("Power operator solution = ",k,"**(1/",p,") = ",k**(1/p))
print("The ratio resultant array")
print(a)
print("Matrix Approximation of the ratios")
for x in range(1,p):
    print(a[x-1]/a[x])