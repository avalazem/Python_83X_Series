# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 07:49:59 2020

@author: Dr. Mark E. Lehr

Purpose:  Function main and others

"""

import math

def futrVal1(pv,i,n):
    return pv*(1+i)**n

def futrVal2(pv,i,n):
    if n==0: return pv
    return futrVal2(pv,i,n-1)*(1+i)
    
def futrVal3(pv,i,n):
    for x in range(0,n):
        pv*=(1+i)
    return pv

def futrVal4(pv,i,n):
    return pv*math.exp(n*math.log(1+i))

def retire1(pv,i,n,d):
    for x in range(0,n):
        pv*=(1+i)
        pv+=d
    return pv

def retire2(pv,i,n,d):
    return futrVal2(pv,i,n)+futrVal2(d/i,i,n)-d/i

def retire3(pv,i,n,d):
    if n==0:return pv;
    return retire3(pv,i,n-1,d)*(1+i)+d


def main():
    pv=100
    i=6.0/100
    n=12
    d=100
    print("Future Value Power = $%.2f" % futrVal1(pv,i,n))
    print("Future Value Power = $%.2f" % futrVal2(pv,i,n))
    print("Future Value Power = $%.2f" % futrVal3(pv,i,n))
    print("Future Value Power = $%.2f" % futrVal4(pv,i,n))
    print("Future Value Power = $%.2f" % retire1(pv,i,n,d))
    print("Future Value Power = $%.2f" % retire2(pv,i,n,d))
    print("Future Value Power = $%.2f" % retire3(pv,i,n,d))
    
main()