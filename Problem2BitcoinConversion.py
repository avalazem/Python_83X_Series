"""
    Name:     Mark
    Date:     January 7th, 2020
    Purpose:  Bitcoin Conversion
    Versions: First and Last
    
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Constant Variable Declaration and Initialization.
CNVBIT=38408.70

#Random Input of the 3 variabls hrs,min,secs
numBits=r.randint(0,10)

#Processs->Map Inputs to Outputs
dollars=numBits*CNVBIT

#EXAMINE RESULTS IN VARIABLE EXPLORER