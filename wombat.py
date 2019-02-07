#!/usr/bin/env python
import othermodule
import getpass
# from getpass import getuser

class Wombat():

    def doit(self):
        print("doit()")
        othermodule.other_function()
        print("in doit() -- getuser() id:", id(getpass.getuser))
        return getpass.getuser()
