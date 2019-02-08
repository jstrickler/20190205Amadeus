#!/usr/bin/env python
# from multiprocessing import Pool
from multiprocessing.dummy import Pool

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()

MAX_SLEEP_TIME = 3

pool = Pool(3)

WORD_LIST = pool.map(str.upper, WORDS)

print(WORD_LIST)
