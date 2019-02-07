#!/usr/bin/env python
from functools import wraps

def spam():
    return 5

x = spam()

def eggs():
    def ham():
        return 10
    return ham

y = eggs()

print(y())

def foo(old_function):

    @wraps(old_function)
    def replacement(*args, **kwargs):
        print("wokka-wokka")
        result = old_function(*args, **kwargs)
        return result

    return replacement


def bark():
    print("Woof woof")


bark = foo(bark)

bark()
print()

@foo
def meow():
    print("meow meow")

# meow = foo(meow)

meow()

@foo
def thing(a, b):
    print("things:", a, b)


thing(1, 2)
print(thing, thing.__name__)


# @deco
# def FUNC():
#    pass
# FUNC = deco(FUNC)
print('-' * 60)
def bar(word_to_print):

    def _temp(old_function):

        @wraps(old_function)
        def replacement(*args, **kwargs):
            print(word_to_print)
            result = old_function(*args, **kwargs)
            return result
        return replacement
    return _temp


@bar('wheee')
def wombat():
    print("I am a wombat")

@bar('whoo-whoo')
def platypus():
    print("I am a platypus")

# platypus = bar('whoo-whoo')(platypus)
wombat()
platypus()
