#!/usr/bin/env python
import pdb

from carddeck import CardDeck
from jokerdeck import JokerDeck

C1 = CardDeck("Leslie")

print(C1.dealer)

C1.dealer = 'Bob'

try:
    C3 = CardDeck({})
    C1.dealer = [None, 3.2]
except TypeError as err:
    print(err)

print(C1.dealer)

print(C1.cards)

hand = []
for i in range(5):
    hand.append(C1.draw())
print("Hand:", hand)

print(C1.get_suits())
print(CardDeck.get_suits())

CardDeck.bark()
print('-' * 60)
J1 = JokerDeck('Jack')
print(J1)
print(J1.draw())
print(J1.cards)

J1.bark()
print(JokerDeck.mro())
print(J1)   # print(str(j1))
print(C1)
print(len(J1))   #  print(str(len(j1)))
print(len(C1))
c2 = CardDeck("Bonnie")

Z = C1 + c2

print(Z)
print(len(Z))
print(Z.draw())

X = c2 + C1
print(X, len(X))
print(X.draw())

pdb.set_trace()

E1 = CardDeck("B")
E2 = CardDeck("B")
print(id(E1), id(E2))
print(E1 == E2)


