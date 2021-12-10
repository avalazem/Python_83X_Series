
#Dr. Mark E. Lehr
#October 18th, 2021
#Mixup or Shuffle

import random as r

#Card Property
face  = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]

#Print the list
print("Original Order")
print(face)

#Mixup the face List by randomly swapping each position
for x in range(0,len(face)):
    rnd=int(r.random()*len(face))
    #Swap 2 cards
    temp=face[x]
    face[x]=face[rnd]
    face[rnd]=temp
    
print("After Mixing up")
print(face)