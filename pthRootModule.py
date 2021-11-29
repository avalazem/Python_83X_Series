#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:16:50 2021

@author: Dr. Mark E. Lehr

Purpose:  Creating a Module consisting of functions
"""
#Importing Numpy for 1 and 2 Dimensional Arrays and math
import numpy as np
import math

#Define a couple of functions to perfrom the above task
def pthRootRec(p,B,a,tol):
    abefore=a[p-2]/a[p-1]
    a=np.matmul(B,a)
    aafter=a[p-2]/a[p-1]
    if math.fabs(aafter-abefore)<tol:
        return aafter
    return pthRootRec(p,B,a,tol)
    
def pthRoot(p,k,tol):
    #Initialize the matrix and vector
    B = np.ones((p,p))
    a = np.ones((p,1))
    #Form B with the Polynomial in k
    for row in range(0,p):
        for col in range(row+1,p):
            B[row][col]=k
    #Return the result when close enough
    return pthRootRec(p,B,a,tol)