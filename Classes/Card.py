
#Dr. Mark E. Lehr
#October 18th, 2021
#Creating a Card Class

class Card:
  def __init__(self, number):
    self.number=number

  def get_number(self):
    return self.number

  def face(self):
    face = ["A","2","3","4","5","6",
            "7","8","9","T","J","Q","K"]
    indx = self.number%13
    return face[indx]

  def suit(self):
    suit = ["S","D","C","H"]
    indx = int(self.number/13)
    return suit[indx]

  def value(self):
    indx=self.number%13+1
    if indx > 10:
      indx=10
    return indx