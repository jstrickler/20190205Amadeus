#!/usr/bin/env python
from carddeck import CardDeck


class Dog():
    def __init__(self, wow):
        print("I am a dog")

    def bark(self):
        print("Woof! Woof!")

class JokerDeck(CardDeck, Dog):
    def bark(self):
        print("Meow!")

    def _create_deck(self):
        super()._create_deck()
        self._cards.append(('J1', 'Joker'))
        self._cards.append(('J2', 'Joker'))
