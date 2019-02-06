#!/usr/bin/env python
from collections import namedtuple



Person = namedtuple('Person', 'first_name last_name product')

Person = namedtuple('Person', ['first_name', 'last_name', 'product'])


person = Person('Bill', 'Gates', 'Microsoft')

print(person[0], person[1])
print(person.first_name, person.last_name)
print(type(person).__name__)

person = 'Bill', 'Gates', 'Microsoft', 'junk', 'wombat', 'pizza'

first_name, last_name, product, *stuff = person

values = ['a', 'b', 'c', 'd', 'e', 'f']

# for v, w in values:
    # v, w = values[0]
    # v, w = values[1]
    # ...
#    pass

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


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

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in airports.items():
    print(abbr, name)
print()

colors = ['red', 'blue', 'green']
for i, color in enumerate(colors):
    print(i, color)
print()

colors = ['red', 'blue', 'green']
for i, color in enumerate(colors, 1):
    print(i, color)
print()

print(list(enumerate(colors)))

def get_lat_lon():
    return 45.233, 123.323

def blech(x):
    return 10 * x


print(blech(45))
x = blech(98)
print(x)
