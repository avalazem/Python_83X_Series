"""
Created on Thu Oct  22 19:23:54 2020

@author: Dr. Mark E. Lehr

Purpose:  Monty Hall Problem

"""

#import the random number generator and set the seed with the date
import random as r
from datetime import datetime as d
r.seed(d.now())

#Take stats
PERCENT=100    #Constant, Percentage conversion
nGames=1000000 #Number of Games to Simulate
nStay=0        #Number of times Game is played and you win by staying
nSwitch=0      #Number of times Game is played and you win by switching

#Create 2 Lists
door=[1,2,3]                             #Door List
typDoor=["Stay","Switch","Door to Open"] #Door Type

#Play any number of Games and keep track of results
for ngames in range(1,nGames+1):
    #Choose the Doors
    r.shuffle(typDoor)         #Radomize the 3 doors
    drPrize  = r.choice(door)  #Random door where prize is located
    prize = door.index(drPrize)#Index of random door where prize is located
    
    #Make sure prize is not behind door to open
    #if True then swap with Switch
    if typDoor[prize]=="Door to Open":  #Can't choose the open door
        prize=typDoor.index("Switch")   #Need to choose the switch door
        
        
    #Count how many times you win by staying or switching
    if   typDoor[prize]=="Stay":     nStay  += 1
    elif typDoor[prize]=="Switch":  nSwitch += 1
    else: print("Logic Error")
        
    if(nGames==1):
        print("Door participant chooses  = ",door[typDoor.index("Stay")])
        print("Door to open              = ",door[typDoor.index("Door to Open")])
        print("Door to switch if offered = ",door[typDoor.index("Switch")])
        print("Door the prize is behind  = ",door[prize])
    
print("The percentage wins if staying  = ",nStay/nGames*PERCENT,"%")
print("The percentage wins if changing = ",nSwitch/nGames*PERCENT,"%")
