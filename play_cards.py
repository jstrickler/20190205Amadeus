#!/usr/bin/env python

from carddeck import CardDeck

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
