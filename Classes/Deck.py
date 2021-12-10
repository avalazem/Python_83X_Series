from Card import Card
import random

#Dr. Mark E. Lehr
#October 18th, 2021
#Creating a Deck Class

class Deck:
    def __init__(self, nCards):
        self.nCards = nCards
        self.cards = []
        self.indx = []
        for x in range(0,nCards):
            self.cards.append(Card(x))
            self.indx.append(x)

    def get_cards(self,idx):
        return self.cards[self.indx[idx]];

    def get_nCards(self):
        return self.nCards

    def shuffle(self,nShuf):
        for x in range(1,nShuf):
            for y in range(0,self.nCards):
                rnd=int(random.random()*self.nCards)
                temp=self.indx[y]
                self.indx[y]=self.indx[rnd]
                self.indx[rnd]=temp