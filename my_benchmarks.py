#!/usr/bin/env python

import timeit

setup_code = """
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]
"""


codes = [
    '''
f1 = [f.upper() for f in fruits]
for fruit in f1:
    x = fruit
    ''',
    '''
f1 = []
for f in fruits:
    f1.append(f.upper())
for fruit in f1:
    x = fruit
    ''',
    '''
f1 = (f.upper() for f in fruits)
for fruit in f1:
    x = fruit
    ''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(1000000))
    print()

