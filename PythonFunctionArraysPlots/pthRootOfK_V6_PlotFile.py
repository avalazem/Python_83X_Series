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
         v6 -> Plotting information from a file
"""

#Importing Numpy for 1 and 2 Dimensional Arrays with Json
import matplotlib.pyplot as plt
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
aHist=np.array(data["aHist"])
print("Data string converted to Dictionary")
print(data)
f.close()

#Display the results
print("The previous resultant array history")
print(aHist)

#Create the Ratio array to plot
row,col=aHist.shape
aRatio=np.ones((col,row-1))
print("Matrix Approximation of the ratios")
for r in range(0,row-1):
    for c in range(0,col):
        aRatio[c][r]=aHist[r][c]/aHist[r+1][c]
        
#Print the array
print(aRatio)

#Prepare legend string for the plot
legendStrs=[]
for c in range(1,col+1):
    legendStrs.append("Column " +str(c))

#Now plot the result
plt.plot(aRatio)
plt.xlabel("Iterations")
strTitle=" "+str(k)+"**(1/"+str(p)+") = "+str(k**(1/p))
plt.ylabel(strTitle)
plt.title("pth Root Appoximation" + strTitle)
plt.grid()
plt.legend(legendStrs,loc ="lower right")
plt.show()

