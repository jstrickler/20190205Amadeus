#!/usr/bin/env python
from pprint import pprint

x = 5

values = 1, 2, 3

def spam():
    y = 42
    print(locals())

g = globals()
pprint(g)

print(g['x'])
print(x)
g['student'] = 'Brian'

print(student)

g['bark'] = lambda : print("Woof!")

bark()

spam()
