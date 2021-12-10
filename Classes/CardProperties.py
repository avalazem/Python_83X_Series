
#Dr. Mark E. Lehr
#October 18th, 2021
#Creating a Card Class

#Card Properties
face  = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
value = [ 1 , 2,  3,  4 , 5,  6,  7,  8,  9, 10, 10, 10, 10 ]
suit  = ["S","D","C","H"]

#Print each card in the deck out by card number
nCards=52
txtFormat="{:>3} {:>6} {:>6} {:>5}"

print("Number of Cards in the Deck =",nCards)
print("Index  Value  Face  Suit")

for crdNum in range(0,nCards):
    f =  face[crdNum%13]
    v = value[crdNum%13]
    s =  suit[int(crdNum/13)]
    print(txtFormat.format(crdNum,v,f,s))