# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:18:27 2022

@author: mlehr
"""

#Query the user for inputs
print("This program calculates the square root")
number=float(input("Input the number: "))
cntLoop=float(input("Number of guesses to make?: "))
accuracy=int(input("The Accuracy in Decimal Places?: "))

#Start the guess and the count
guess=number/10
cnt=1
tolerance=10**(-accuracy)
step=0.1;

#Loop until done
while abs(number-guess*guess)>tolerance and cnt <= cntLoop:
    print("The square root of (",number,") = ",guess,"on",cnt,"guess/es")
    guess=guess+step
    if guess*guess>number:
        guess-=step
        step/=10
    cnt+=1
    
#Compare the results
print("The final approximation =",guess)
print("The actual answer =",number**(0.5))