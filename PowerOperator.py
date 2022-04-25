# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:31:55 2022

@author: mlehr
"""

#Declare variables and initialize
#Prompt the user for inputs
print("Program Calculates x^y")
print("Input x and y")
#Receive the inputs
op1=int(input())  #Operand 1 no units
op2=int(input())  #Operand 2 no units

#Determine the power of x^y
result=op1**op1  #Result of x**y the power operator

#Display the results
print()
print("The results are")
print(result," = ",op1,"**",op2)