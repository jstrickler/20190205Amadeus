#!/usr/bin/env python
from copy import deepcopy

x = 5

y = x

m = [1, 2, 3]
n = m
n.append(88)
print(m)
c1 = list(m)  # new list
c2 = m[::]  # 100% slice



c3 = deepcopy(c1)
c3.append(99)
print(c1, c3)


stuff = [[1, 2, 3], ['a', 'b', 'c']]

s1 = list(stuff)

s1[0].append(88)

print(stuff)
print()

s2 = deepcopy(stuff)

s2[0].append("hello")
print(stuff)
print(s2)


name = 'DeadBeef'
count = 5

# print(name + count)
# print(count + name)

print(name + name)
print(count + count)

print(name + str(count))

print(count + int(name, 16))


print(count, name, 88, sep='/', end='wowie')
print()

import sys

print("Your hair's on fire!", file=sys.stderr)

print("%s %d" % (name, count))  # legacy python 2
print("{} {}".format(name, count))  # python 3
print(f"{name:>25s} {count:013d}")  # f-string 3.6+

a = 2
b = 7
print(f"Sum of {a} and {b} is {a + b}")

n = 2309582093582
print(f"{n:,d}")

n = 203985209385209385209385209385029385209385209385209358209358203958203985209358203958029385029385029385029385029850298350289350982059820395820935820935820938502985029835

print(n)

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""  # triple-delimited (AKA triple-quoted)
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string
fake_meat = 'spam'
s6 = f"{fake_meat}\n"

print("Guido's the boss")
print('The "boss" is Guido')
print("""Guido's the "boss" forever""")


actor = "Liam Neeson"

print(actor.upper(), actor.lower())
print(actor.count('n'))
print(actor.count('N'))
print(actor.lower().count('n'))

import re
print(len(re.findall('n', actor, re.I)))

s = "aiaiaiaiLiam Neesoniaiaiaia"
print('|' + s.lstrip('ia') + '|')
print('|' + s.rstrip('ia') + '|')
print('|' + s.strip('ia') + '|')


s = "         Liam Neeson          "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')

words = ['dog', 'bites', 'man']

phrase = ' '.join(words)
print(phrase)
print('/'.join(words))

print(phrase.split())

giant_speech = 'fee:fi:fo:fum'
print(giant_speech.split(':'))

print(giant_speech.split(':', 1))

x = b'what is this?'
print(x)


weather = "50\u00B0"

print(weather)

wb = weather.encode()
print(wb)

w = wb.decode()
print(w)

x = [5, 10, 'zombie', 4.3]

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[-1], fruits[len(fruits) - 1])

print(fruits[:5])
print(fruits[3:9])
print(fruits[::2])
print(fruits[1::2])

print(fruits)
fruits[2:4] = ["pineapple", 'tamarind', 'tomato', 'eggplant']
print(fruits)


print(fruits[-5:])

print(fruits[::])

fruits[4] = "Leeloo"

print(fruits[4])

x = ['a', 'b', 'c']
y = ['m', 'f']

x.extend(y)
print(x)

x.append('q')
print(x)

x.insert(0, 'r')
x.insert(4, 'p')
print(x)

i = x.pop()
print(i)
print(x)

i = x.pop(2)
print(i, x)

del x[2]
print(x)

x.remove('f')
print(x)

print(x.index('a'))

letter = 'z'
if 'z' in x:
    print(x.index('z'))
else:
    print(f"{letter} not found")

print("am" in actor)

print("Not" in actor)

for letter in x:
    print(letter)

# for VAR ... in ITERABLE:
#     pass


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

print(airports['EWR'])
print(airports.get('BOS'))
print(airports.get('BOS', 'NOT FOUND'))
print(airports.setdefault('BOS', 'Boston'))
print(airports)

more_airports = {'ELM': 'Elmira/Corning', 'MCH': 'Manchester', 'RDU': 'Durham/Raleigh'}

airports.update(more_airports)

print(airports)

print(airports.keys())
print(airports.values())

for airport_abbr, airport_name in airports.items():
    print(airport_abbr, airport_name)

print(list(airports.items()))

airports['PVD'] = 'Providence'

print(airports)

print(len(x), len(airports))

print(airports.items())

cities1 = ['Paris', 'Marseilles', 'Toulouse', 'Nice']

cities2 = ['Nice', 'Toulouse', 'Lyon']

c1 = set(cities1)
c2 = set(cities2)

print("both:", c1 & c2)  # intersection
print("just one:", c1 ^ c2) # xor (non-intersection)
print("all:", c1 | c2)  # union
print("just c1:", c1 - c2)
print("just c2:", c2 - c1)

food = ['spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'eggs', 'oeufs',
        'coq au vin', 'pate', 'pate', 'pate']
print(set(food))
