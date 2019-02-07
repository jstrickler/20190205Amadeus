#!/usr/bin/env python
import random

def main():
    c = CardDeck("Belinda")
    print(c)
    print(CardDeck.mro())  # method resolution order

class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._cards = None
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                card = r, s
                self._cards.append(card)
        random.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards


    # def get_dealer(self):
    #     return self._dealer

    @property  # getter property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def spam(self):
        return self._spam

    @spam.setter
    def spam(self, value):
        self._spam = value

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def bark():
        print("Woof! woof!")

    def __len__(self):  # implements  len()
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return "{}: {}".format(my_name, len(self))

    def __add__(self, other):
        if isinstance(self, type(other)):
            tmp = type(self)(self.dealer)
            tmp._cards += other.cards
            return tmp
        else:
            raise TypeError("Cannot mix deck types")

    def __eq__(self, other):
        return set(self.cards) == set(other.cards)
        # return self.cards == other.cards

if __name__ == '__main__':
    main()
