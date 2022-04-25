# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:38:03 2022

@author: mlehr
"""

#Create Different Types of Variables
xInt=8
yFloat=3.2
zString="This is a test"

#Explore the different techniques of formatting output
xstr="The integer value of x = {:<10.3f}  Just to extend."
ystr="The floating value of y = {:<10.2e}  Just to extend."
zstr="The string = \'{:^20}\'   Just to extend."
allstr="{} {} {}"

#Output using the above format
print(xstr.format(xInt))
print(ystr.format(yFloat))
print(zstr.format(zString))
print(allstr.format(yFloat,xInt,zString))