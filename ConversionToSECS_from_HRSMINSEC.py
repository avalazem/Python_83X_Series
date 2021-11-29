"""
    Name:     Mark
    Date:     June 24th, 2021
    Purpose:  Conversion Hrs, Mins, Secs to Seconds
    Versions: First and Last
    
"""

#Input the 3 variabls hrs,min,secs
#Convert Strings to Floats
secs=float(input("Input the Number of Seconds!\n"))
mins=float(input("Input the Number of Minutes!\n"))
hrs=float(input("Input the Number of Hours!\n"))

#Variable Declaration, sometimes Declaration and Initialization can occur at one time.
CNVM2S=60  #60 Seconds in every Minute
CNVH2M=60  #60 Minutes in every Hour

#Processs->Map Inputs to Outputs
totSecs = secs + mins * CNVM2S + hrs * CNVH2M * CNVM2S

#Output Results -> Include Format for Inputs/Outputs
print("The total number of seconds =",totSecs)