# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:37:41 2022

@author: mlehr
"""

#import the random number generator and set the seed
import random as r
from datetime import datetime as d
r.seed(d.now())

#Loop 1000 times to see how often each student wins the cake
aWins=bWins=cWins=0
nGames=1000000
percent=100
for game in range(1,nGames+1):

    #Fill the list with random numbers
    aOut=True
    aWorks=1.0/3
    bOut=True
    bWorks=1.0/2
    cOut=True
    cWorks=1.00

    while aOut+bOut+cOut > 1:
        if(r.uniform(0,1) <= aWorks and aOut):
            if(cOut):cOut=False
            elif(bOut): bOut=False
        if(r.uniform(0,1) <= bWorks and bOut):
            if(cOut):cOut=False
            elif(aOut): aOut=False
        if(r.uniform(0,1) <= cWorks and cOut):
            if(bOut):bOut=False
            elif(aOut): aOut=False

    if(aOut):aWins+=1
    if(bOut):bWins+=1
    if(cOut):cWins+=1

#Display the results
print("Total Number of Games =",aWins+bWins+cWins)
print("A wins ",aWins/nGames*percent,"%")
print("B wins ",bWins/nGames*percent,"%")
print("C wins ",cWins/nGames*percent,"%")