#!/usr/bin/env python
import ham

class Spam():  # <2>
    def __init__(self):
        self._value = ham.ham()  # <3>

    @property
    def value(self):  # <4>
        return self._value
