#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

c1 = CardDeck("Leslie")

print(c1.dealer)

c1.dealer = 'Bob'

try:
    c3 = CardDeck({})
    c1.dealer = [None, 3.2]
except TypeError as err:
    print(err)

print(c1.dealer)

print(c1.cards)

hand = []
for i in range(5):
    hand.append(c1.draw())
print("Hand:", hand)

print(c1.get_suits())
print(CardDeck.get_suits())

CardDeck.bark()
print('-' * 60)
j1 = JokerDeck('Jack')
print(j1)
print(j1.draw())
print(j1.cards)

j1.bark()
print(JokerDeck.mro())
print(j1)   # print(str(j1))
print(c1)
print(len(j1))   #  print(str(len(j1)))
print(len(c1))
c2 = CardDeck("Bonnie")

z = c1 + c2

print(z)
print(len(z))
print(z.draw())

x = c2 + c1
print(x, len(x))
print(x.draw())

e1 = CardDeck("B")
e2 = CardDeck("B")
print(id(e1), id(e2))
print(e1 == e2)


