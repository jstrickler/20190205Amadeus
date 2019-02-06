#!/usr/bin/env python

class Spam():
    def __init__(self):
        self.color = 'blue'
        self.mode = None

s1 = Spam() #   Spam s1 = new Spam();

print(s1, type(s1))

foom = type(s1)

s2 = foom()

print(s2)

print(dir(s1))

print(s1.color)
