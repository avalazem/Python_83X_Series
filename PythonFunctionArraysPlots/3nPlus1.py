# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:59:45 2020

@author: mlehr
"""

#Import needed libraries
import math
import time

#Set the initial number to check
mInit = int(18*math.log(10)/math.log(3)+1)

#Loop on 3n+1
for m in range(mInit+100,mInit+101):
    test=2*3**m+1
    print("2 * 3**",m,"+ 1 = ")
    time.sleep(10)
    while test != 1:
        if(test%2==0):
            test>>=1
        else:
            t=test<<1
            test=t+test+1
        print(test)
    test1=2**m+1
    print("2**",m,"+ 1 = ")
    time.sleep(10)
    while test1 != 1:
        if(test1%2==0):
            test1>>=1
        else:
            t=test1<<1
            test1=t+test1+1
        print(test1)