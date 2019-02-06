#!/usr/bin/env python
import sys

import amatools  # find and execute amatools.py

amatools.book_flight()
amatools.get_user_names()

# amatools._read_config()
print(amatools.CITIES)

amatools.CITIES = 123
print(amatools.CITIES)
print()

for path in sys.path:
    print(path)
print()

print(sys.prefix)
print(sys.executable)

