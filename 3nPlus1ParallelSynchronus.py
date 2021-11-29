# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:59:45 2020

@author: mlehr
"""

#Import needed libraries
import math
import time
import multiprocessing as mp
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

#Set the initial number to check - 10^18
mInit = int(18*math.log(10)/math.log(3)+1)

#3n+1 function at certain test points
def nPlus1(counter,mStart = 37):
    mCount=mStart+int(counter/3)
    m23rds=int(mCount*2/3)
    string=""
    if(counter%3==0):
        test=2*3**mCount+1
        string+="2 * 3 ** "+str(mCount)+"+ 1 = "
        mpow=3**m23rds
    elif(counter%3==1):
        test=2**mCount+1
        string+="2 ** "+str(mCount)+"+ 1 = "
        mpow=2**m23rds
    else:
        test=2*3**mCount+2**mCount-1
        string+="2 * 3 ** "+str(mCount)+" + ""2 ** "+str(mCount)+"+ 1 = "
        mpow=3**m23rds
        
    #The integer sequence generator
    while test > mpow:
        if(test%2==0):
            test>>=1
        else:
            t=test<<1
            test=t+test+1
        #print(test)
        
    return string
    

#In order for multiprocessing to work need this line
if __name__ == '__main__': 
    #Setup the number of threads for Parallel Processing
    percent=25/100;
    thrds=int(percent*mp.cpu_count())
    print("Number of Threads =",thrds,"@",percent*100,"%")
    results = []
    
    #Do a little test before hand, should take about 4 seconds
    startTime=time.time()
    for counter in range(7000,9000):
        results.append(nPlus1(counter,mInit))
    endTime=time.time()
    
    #Print a segment of the results then clear and make sure it is clear
    print(results[-6:])
    print(int(endTime-startTime),"secs")
    
    results.clear()
    
    print(results[-6:])
    
    # Step 1: Init multiprocessing.Pool() and the time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)	
    startTime=time.time()
    
    pool = mp.Pool(processes=thrds) 
    
    # Step 2: `pool.apply` Set up the list comprehension
    #results_async = [pool.apply_async(nPlus1, args=(counter,mInit)) for counter in range(138000,154000)]
    results_async = [pool.apply_async(nPlus1, args=(counter,mInit)) for counter in range(0,15000)]
    
    # Step 3: Don't forget to close
    pool.close()    
    
    #Extremely important, this synchonizes the results
    results = [r.get() for r in results_async] 
    print(results[-6:])
    
    #How long did this take?
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)	
    endTime=time.time()
    print(int(endTime-startTime),"secs")