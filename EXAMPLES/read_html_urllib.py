#!/usr/bin/env python

import urllib.request

response = urllib.request.urlopen("https://www.python.org")

print(response.info())  # <1>
print()

print(response.read(5000).decode())   # <2>
