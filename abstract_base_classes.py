#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

    def fly(self):
        print("Wheeee")

class Dog(Animal):
    def move(self):
        pass

d = Dog()
print(d)
d.move()
d.fly()

class Spam():
    pass

class Foom(Animal, Spam):
    pass

print(Foom)
print(dir(Animal))
print(dir(Dog))

