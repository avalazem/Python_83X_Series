"""
    Name:     Mark
    Date:     June 24th, 2021
    Purpose:  Conversion Feet to Miles
    Versions: First and Last
    
"""

#Input the # of Feet
#Convert Strings to Floats
feetIn=float(input("Input the Number of Feet!\n"))

#Variable Declaration, sometimes Declaration and Initialization can occur at one time.
CNVFTMLS=5280  #5280 feet per mile


#Processs->Map Inputs to Outputs
mileOut=feetIn/CNVFTMLS

#Output Results -> Include Format for Inputs/Outputs
print("The total number of Miles =",mileOut)