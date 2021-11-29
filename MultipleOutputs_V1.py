# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:54:27 2020

@author: mlehr

Purpose:  Functions with multiple outputs
"""

def query():
    person={}
    name=input("Input your Name or type Quit: ")
    if name=="Quit":return 
    person["Name"]=name
    person["Age"]=int(input("Input your Age: "))
    return person

def fillst(lstNum):
    nameLst=[]
    for x in range(0,lstNum):
        lst=query()
        if lst==None:break
        nameLst.append(lst)
    return nameLst

    
def display(lstArray):
    for x in lstArray:
        print(x["Name"],"is",x["Age"],"yrs old")
            
            

display(fillst(2))