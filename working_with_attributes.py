#!/usr/bin/env python
from types import MethodType

from ANSWERS.president import President

p = President(26)

print(p.last_name)

print(dir(p))
print()

fields = ['birth_date', 'death_date']

for field in fields:
    print(getattr(p, field))

# getattr() hasattr() setattr() delattr()

def bark(self):
    print("Woof woof")

def meow(self):
    print("Meow meow purr")

setattr(President, 'bark', bark)

p.bark()

for attribute in dir(p):
    if attribute.startswith('_'):
        continue

    value = getattr(p, attribute)
    print(attribute, value)

setattr(p, 'meow', MethodType(meow,p))


p.meow()
p.bark()

t = President(45)
t.bark()
# t.meow()

x = None

if hasattr(x, 'to_json'):
    x.to_json()

if hasattr(p, 'wombat'):
    print(getattr(p, 'wombat'))
