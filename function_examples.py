#!/usr/bin/env python
from typing import Iterable, List



def spam(values: Iterable[int]) -> List[int]:
    pass

def zero():
    return 0

def nothing():
    pass


n = nothing()
print(n)

print(zero())
x = 5
x = 'Bob'

class Spam():
    pass

def func1(a: int, b: Spam) -> None:
    # if not isinstance(a, int):
    #     raise TypeError("expected int")
    print(a, b)


func1(5, 6)

func1(x, 'bar')

def func2(a, b, *c):
    print(a, b, c)

func2(1, 2, 3, 4, 5, 6, 7)

def func3(*args):
    print(args)

def func4(a, b=10):
    print(a, b)

func4(20, 30)
func4(100)


def func5(*, file_name, user_name):
    print(file_name, user_name)

func5(file_name='spam.txt', user_name='Womboid')
print()

def open(file_name, *, codec='utf-8', mode='r'):
    print(file_name, codec, mode)

x = open('foo.txt')
x = open('foo.txt', mode='w', codec='ascii')


# x = sorted(foo, key=some_func)


def junk(value=None):
    pass

def config(**values):
    print(values, '\n')

config(animal="wombat", color='pink', city='Lyon')

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass


def generic(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print()


generic()
generic(1, 2, 3)
generic(1, 2, 3, foo=4, bar=5, animal='wombat')
generic(foo=4, bar=5, animal='wombat')










