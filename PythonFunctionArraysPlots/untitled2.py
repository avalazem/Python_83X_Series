# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:21:14 2022

@author: mlehr
"""

sign=-1
print(sign)
cnt1=1
cnt2=1
for x in range(0,10):
    signres=sign**x
    cnt1+=1
    cnt2+=2
    print(signres," ",cnt1," ",cnt2)