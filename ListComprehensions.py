"""
Created on Mon Oct  5 08:46:31 2020

@author: mlehr
"""
start=0
stopMinus1=11
step=2
    
nList=list(range(start,stopMinus1,step))
print(nList)

squares=[value**2 for value in range(1,11,2)]
print(squares)

value=[value**0.5 for value in squares]
print(value)