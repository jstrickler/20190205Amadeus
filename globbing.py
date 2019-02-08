#!/usr/bin/env python
from glob import glob

files = glob('/etc/p*')
print(files)
print('-' * 60)

files = glob('/ama/deus*')
print(files)
print('-' * 60)

files = glob('/wombat')
print(files)
print('-' * 60)
