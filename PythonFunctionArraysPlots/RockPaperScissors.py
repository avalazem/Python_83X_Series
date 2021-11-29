# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:22:41 2021

@author: mlehr
"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#What are the choices in this game?
choice=["Rock","Paper","Scissors"]#List to hold possible positions

#Let the computer choose which to pick
computer=choice[r.randint(0,2)]       #Computer makes random choice
print("The computer chooses",computer)#Print the choice made by the computer

#Let Mark choose which to pick
mark=choice[r.randint(0,2)]           #Mark makes random choice
print("Mark Lehr    chooses",mark)    #Print the choice made by Mark

#Display the Winner
if mark==computer:             #Display tie if the same for each
    print("A Tie is accomplished!")
elif mark == "Scissors" and computer == "Paper":
    print("Mark is the Winner")#Scissors beats Paper
elif mark == "Paper"    and computer == "Rock":
    print("Mark is the Winner")#Paper beats Rock
elif mark == "Rock"     and computer == "Scissors":
    print("Mark is the Winner")#Rock beats Scissors
else:                          #Computer wins all other options left
    print("The Computer is the Winner")