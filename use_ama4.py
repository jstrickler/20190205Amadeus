#!/usr/bin/env python
import amadeus

print(amadeus)
print(dir(amadeus))

import amadeus.flight

print(dir(amadeus.flight))

amadeus.amatools.book_flight()
