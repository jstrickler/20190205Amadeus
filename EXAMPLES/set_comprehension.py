#!/usr/bin/env python

import re

with open("../DATA/alice.txt") as mary_in:
    s = {w.lower()  for ln in mary_in  for w in re.split(r'\W+', ln) if w} #<1>
print(sorted(s))
print(len(s))
print(max(s, key=len))

# NEW_LIST = [EXPR for VAR in ITERABLE if CONDITION]
# NEW_DICT = {KEY_EXPR: VALUE_EXPR for VAR in ITERABLE if CONDITION}
# NEW_SET = {EXPR for VAR in ITERABLE if CONDITON}



