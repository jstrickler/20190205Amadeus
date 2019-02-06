#!/usr/bin/env python
"""
Example of Python scope for my excellent Amadeus students

They are the best students, ever. Probably.
"""
import sys

# def print(*args, **kwargs):
#     sys.stdout.write("HA HA HA\n")

name = 'Fred Flintstone'  # global

def doit():
    """
    Set some stuff

    :return: None
    """
    town = 'Bedrock'  # local
    print("town is", town)
    print("name is", name)


doit()
town = 'Durham'

print("town is", town)
animal = 'wildebeest'

def outer():
    """
    Nested function example

    :return: Function which prints nonlocal data
    """
    animal = 'capybara'

    def inner():
        animal = 'honey badger'
        print("animal is", animal)

    return inner


f = outer()
f()

#  local nonlocal global builtin

def cook(recipe, servings):
    """
    Cook something delicious

    :param recipe: Cooking algorithm
    :param servings: Cooking result
    :return: A tasty dish
    """
    pass

cook()
