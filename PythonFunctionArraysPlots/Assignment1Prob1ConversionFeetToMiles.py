"""
    Name:     Mark
    Date:     September 2nd, 2021
    Purpose:  Conversion Feet to Miles
    Versions: First and Last
    
"""

#Input the 3 variabls hrs,min,secs
#Convert Strings to Floats
print("This Program Converts feet to miles.")
feetIn=float(input("Input the Number of Feet!\n"))

#Variable Declaration, sometimes Declaration and Initialization can occur at one time.
CNVM2F=5280  #Number of feet in a mile

#Processs->Map Inputs to Outputs
mileOut = feetIn/CNVM2F

#Output Results -> Include Format for Inputs/Outputs
print(feetIn," feet = ",mileOut," miles")