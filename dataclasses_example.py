#!/usr/bin/env python
from dataclasses import dataclass

class OldPerson():
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    def __str__(self):
        return f"Person({self._first_name}, {self._last_name})"

    def __repr__(self):
        return "HAHAHA"

p1 = OldPerson('Mary', 'Smith')
p2 = OldPerson('Bob', 'Russel')

print(p1)
print(p1.first_name)

print(repr(p1))

@dataclass(bool=True, frozen=True, order=True)
class Person:
    first_name: str=None
    last_name: str=None

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person('Brian', 'Jarvis')
p2 = Person(last_name='Baudemont', first_name='Adrien')
p3 = Person("Shruti")

print(p1)
print(p2)
print(p3)

print(p2.get_name())

x = Person('Joe', 'Coder')
y = Person('Joe', 'Coder')
print(id(x), id(y))
print(x == y)
print(x is y)

# p1.last_name = "Smith"

print(p1)
