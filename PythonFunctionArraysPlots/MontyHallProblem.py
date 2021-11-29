"""
Created on Thu Oct  14 19:23:54 2020

@author: Dr. Mark E. Lehr

Purpose:  Monty Hall Problem

"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())


#Choose the Doors
stay   = r.randint(1,3)#Random door player chooses
switch = r.randint(1,3)#Random door player could switch if offered
prize  = r.randint(1,3)#Random door where prize is located
dr2Opn = r.randint(1,3)#Random door to open
    
#Make sure doors are unique
while dr2Opn == stay or dr2Opn == prize:
    dr2Opn = r.randint(1,3)
        
#Determine the available door to switch to if offered
while switch==stay or switch==dr2Opn:
    switch=r.randint(1,3)
        
print("Door participant chooses     = ",stay)
print("Door the prize is behind     = ",prize)
print("Door to open                 = ",dr2Opn)
print("Door to switch to if offered = ",switch)