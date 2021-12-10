# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:20:34 2021

@author: mlehr
"""

from Card import Card

nCards=52
txtFormat="{:>3} {:>6} {:>6} {:>5}"

print("Number of Cards in the Deck =",nCards)
print("Index  Value  Face  Suit")

for x in range(0,nCards):
    z=Card(x)
    print(txtFormat.format(x,z.value(),z.face(),z.suit()))
