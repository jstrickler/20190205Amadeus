#!/usr/bin/env python

def spam(a, b, c):
    print(a, b, c)


spam(5, 10, 15)

values = 2, 4, 6

spam(*values)

#  ham(**some_dict)

def blech(*, animal, city, color):
    print(animal, color, city)

blech(animal='wombat', city='Canberra', color='pink')

d = {'animal': 'fennec fox', 'city': 'Paris', 'color': 'lime'}

blech(**d)
