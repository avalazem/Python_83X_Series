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
         v4 -> Write to a file
         v5 -> Read from a file
"""

#Importing Numpy for 1 and 2 Dimensional Arrays with Json
import numpy as np
import json

#Read the string data from the file
f=open("pthRoot.dat","r")
dataStr=f.read()
print("Dictionary String:",dataStr)
#Create the dictionary string
data=json.loads(dataStr)
#Load the data back into the individual variables
p=data["p"]
k=data["k"]
tol=data["tol"]
B=np.array(data["B"])
a=np.array(data["a"])
aHist=np.array(data["aHist"])
print("Data string converted to Dictionary")
print(data)
f.close()

#Display the results
print("Power operator solution = ", k,"**(1/",p,") = ",k**(1/p))
print("The polynomial array")
print(B)
print("The ratio resultant array")
print(a)
print("The previous resultant array history")
print(aHist)
print("Matrix Approximation of the ratios")
for x in range(1,p):
    print(a[x-1]/a[x])