#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f0 = []
for f in fruits:
    if f.startswith('p'):
        f0.append(f.upper())
print("f0:", f0, '\n')

f0 = []
for f in fruits:
    if f.startswith('p'):
        f0.append(f)
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')
#  [EXPR for VAR ... in ITERABLE if COND ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

d = {'*': 5, '-': 10, '+': 8}

s = [k * v for k, v in d.items()]
print("s:", s, '\n')

f4 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 6]
print("f4:", f4, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'cheese',
        'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'eggs', 'oeufs']

food2 = [f for f in food if f not in ('spam', 'cheese')]
print("food2:", food2, '\n')

x = "foo" "bar"

squares = [n ** 2 for n in range(10)]
print("squares: {}".format(squares), '\n')

def double(x):
    return x * 2

doubles = [double(n) for n in range(10)]
print("doubles: {}".format(doubles), '\n')

suits = 'Clubs Diamonds Hearts Spades'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [(r, s) for s in suits for r in ranks]
print("cards: {}".format(cards), '\n')

import os
import glob
files = glob.glob('DATA/*.txt')
print(files)

file_info = {os.path.basename(f): os.path.getsize(f) for f in files}
print("file_info: {}".format(file_info), '\n')

fg1 = (f.upper() for f in fruits)
fruits.append('tomato')
fruits.append('pineapple')

print('fg1:', fg1, '\n')
for f in fg1:
    print(f, end=' ')
print('\n')


with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

def trimmed(file_name):
    with open('DATA/mary.txt') as mary_in:
        for raw_line in mary_in:
            yield raw_line.rstrip()

t = trimmed('DATA/mary.txt')
for line in t:
    print(line)
print()

t = trimmed('DATA/mary.txt')
print(next(t))
print(next(t))

# for x in y: pass
# while True:
#     try:
#         x = next(y)
#     except StopIteration:
#         break

def weird():
    yield "Python"
    yield "is"
    yield "fun"


for x in weird():
    print(x)








