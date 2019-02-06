#!/usr/bin/env python
from amadeus.flight.amatools import get_user_names, CITIES
from amadeus.flight import amatools

get_user_names()
amatools.book_flight()
print(CITIES[0])

