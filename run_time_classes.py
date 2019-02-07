#!/usr/bin/env python

def whoop(cls):
    print("Whoopieeeeeee")

class Dog():
    def bark(self):
        print("Woof! Woof!")

    @classmethod
    def whoop(cls):
        print("Whoopieeeeeee")

d = Dog()
d.bark()



Cat = type('Cat', (), {'meow': lambda self: print("Meow!"), 'breed': 'Persian',
            'whoop': classmethod(whoop)})

c = Cat()
c.meow()
print(c.breed)
c.whoop()
Cat.whoop()
