"""
    Name:     Mark
    Date:     January 7th, 2021
    Purpose:  Conversion Hrs, Mins, Secs to Seconds
    Versions: First and Last
    
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Constant Variable Declaration and Initialization.
CNVM2S=60  #60 Seconds in every Minute
CNVH2M=60  #60 Minutes in every Hour
MAXHRS=24  #24 Hours in every Day

#Random Input of the 3 variabls hrs,min,secs
secs=r.randint(0,CNVM2S)
mins=r.randint(0,CNVH2M)
hrs=r.randint(0,MAXHRS)

#Processs->Map Inputs to Outputs
totSecs = secs + mins * CNVM2S + hrs * CNVH2M * CNVM2S

#EXAMINE RESULTS IN VARIABLE EXPLORER