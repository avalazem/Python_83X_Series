# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 06:36:39 2021

@author: mlehr
"""

#Declare and Initialize Variables
MN2SCS  = 60 #Minutes to Seconds Conversion
HRS2SCS = 60 * MN2SCS #Hours to Seconds Conversion

#Input
secs=int(input("Input Number of Seconds as an integer\n"))
mins =int(input("Input Number of Minutes as an integer\n"))
hrs =int(input("Input Number of Hours as an integer\n"))
      
#Process
numSecs = secs + mins * MN2SCS + hrs * HRS2SCS

#Output
print("The total number of seconds =",numSecs)