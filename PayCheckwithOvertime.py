# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:08:22 2021

@author: mlehr
"""

#Declare and initialize variables
hrsWrkd=60  #Hours worked in hrs
payRate=10  #Pay Rate in $'s/hour
ovrTm1=40   #Overtime between straight and double time
ovrTm2=50   #Overtime when triple pay starts

#Output the intial conditions
print("Number of hours worked = ",hrsWrkd," hrs")
print("Payrate = $",payRate,"/hr")

#Calculations
payChk=hrsWrkd*payRate
hrsWrkd-=ovrTm1
payChk+=hrsWrkd*payRate if hrsWrkd > 0 else 0
hrsWrkd-=(ovrTm2-ovrTm1)
payChk+=hrsWrkd*payRate if hrsWrkd > 0 else 0

#Output the pay check
print("Your Pay Check = $",payChk)