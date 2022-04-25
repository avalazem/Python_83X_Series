# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:23:58 2022

@author: mlehr
"""

#Query the user for inputs
print("This program calculates the square root")
number=float(input("Input the number: "))
cntLoop=float(input("Number of guesses to make?: "))
accuracy=int(input("The Accuracy in Decimal Places?: "))

#Start the guess and the count
guess=number/3
cnt=1
tolerance=10**(-accuracy)

#Loop until done
while abs(number-guess**3)>tolerance and cnt <= cntLoop:
    print("The square root of (",number,") = ",guess,"on",cnt,"guess/es")
    guess=2.0*guess/3.0+number/3.0/guess/guess
    cnt+=1
    
#Compare the results
print("The final approximation =",guess)
print("The actual answer =",number**(1.0/3))