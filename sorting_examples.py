#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0", f0, '\n')

f1 = sorted(fruits, key=str.lower)
print("f1:", f1, '\n')

def ignore_case(f):
    return f.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2: {}".format(f2), '\n')

f3 = sorted(fruits, key=len)
print("f3: {}".format(f3), '\n')

def by_len_then_name(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=by_len_then_name)
print("f4: {}".format(f4), '\n')

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

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(a):
    return a[1], a[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()


for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print()


#  lambda param ... : return-value

values = [2, 5, "29", 'abc', 8, 1, "15", 12]

def compare_by_int_value(e):
    try:
        i = int(e)
    except ValueError:
        i = -1000000

    return i

print(sorted(values, key=str))
print(sorted(values, key=compare_by_int_value))


