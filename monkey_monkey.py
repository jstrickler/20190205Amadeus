#!/usr/bin/env python
import othermodule
from wombat import Wombat
import getpass

getpass.getuser = lambda : "MONKEY-USER"

print("in main -- getuser() id:", id(getpass.getuser))

othermodule.other_function = lambda: print("MONKEY!")

w = Wombat()
u = w.doit()
print(u)

