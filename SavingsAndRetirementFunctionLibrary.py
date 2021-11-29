# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:32:03 2020

@author: mlehr

Purpose:  Library of Savings and Retirement Functions
"""

import math

def savings1(p,i,n):
    return p*(1+i)**n

def savings2(p,i,n):
    for n in range(0,n):
        p*=(1+i)
    return p

def savings3(p,i,n):
    return p*math.exp(n*math.log(1+i))

def savings4(p,i,n):
    if n<=0:return p
    return savings4(p,i,n-1)*(1+i)

def retire1(p,i,n,d):
    return p*(1+i)**n+d/i*(1+i)**n-d/i

def retire2(p,i,n,d):
    return savings4(p+d/i,i,n)-d/i

def retire3(p,i,n,d):
    if n==0:return p
    return retire3(p,i,n-1,d)*(1+i)+d