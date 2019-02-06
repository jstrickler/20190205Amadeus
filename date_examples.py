#!/usr/bin/env python

from datetime import datetime, date, timedelta

today = date.today()

john_bd = date(1956, 10, 31)

print(today, john_bd)
print(today.year, john_bd.year)

john_raw_age = today - john_bd
print(john_raw_age)
print(type(john_raw_age))

print(john_raw_age.days)
print(round(john_raw_age.days / 365, 1))

now = datetime.now()

then = datetime(2018, 11, 23, 16, 32, 1)
print(now, then)

fortnight = timedelta(14)

then = today + fortnight
print(then)


td = datetime.now() - datetime(2019, 2, 5, 10, 14, 37, 38923)
print(td)

import time

then = time.time()
print(then)
time.sleep(3.5)
now = time.time()
print(now)
print((now - then) / 60)
