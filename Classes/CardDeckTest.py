# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:20:34 2021

@author: mlehr
"""

from Deck import Deck

nCards=52
y=Deck(nCards)
txtFormat="{:>3} {:>6} {:>6} {:>5}"

print("Number of Cards in the Deck =",y.nCards)
print("Index  Value  Face  Suit")

for x in range(0,nCards):
    z=y.get_cards(x)
    print(txtFormat.format(x,z.value(),z.face(),z.suit()))

y.shuffle(7)
print("After Shuffle")
print("Index  Value  Face  Suit")

for x in range(0,nCards):
    z=y.get_cards(x)
    print(txtFormat.format(x,z.value(),z.face(),z.suit()))

