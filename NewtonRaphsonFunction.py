# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:18:27 2022

@author: mlehr
"""

#Define the Newton Raphson Square Root function
def sqRoot(number, cntLoop, accuracy):
    #Start the guess and the count
    guess=number/2
    cnt=1
    tolerance=10**(-accuracy)

    #Loop until done
    while abs(number-guess*guess)>tolerance and cnt <= cntLoop:
       guess=guess/2.0+number/(2.0*guess)
       cnt+=1
      
    #Return the result    
    return guess
    

#Query the user for inputs
print("This program calculates the square root")
number=float(input("Input the number: "))
cntLoop=float(input("Number of guesses to make?: "))
accuracy=int(input("The Accuracy in Decimal Places?: "))

    
#Compare the results
print("The final approximation =",sqRoot(number,cntLoop,accuracy))
print("The actual answer =",number**(0.5))