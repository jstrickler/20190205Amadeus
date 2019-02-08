#!/usr/bin/env python
import sqlite3
from dataclasses import dataclass
from datetime import date
from typing import Union

@dataclass(frozen=True)
class President():
    first_name: str
    last_name: str
    birth_date: date
    death_date: Union[date, None]
    start_date: date
    end_date: Union[date, None]
    birth_state: str
    birthplace: str
    party: Union[None,str]

p1 = President(
    'George',
    'Washington',
    date(1732,2,22),
    date(1799,12,14),
    date(1789,4,30),
    date(1797,3,4),
    'Virginia',
    'Westmoreland County',
    None,
)

print(p1, '\n')

p2 = President(
    'Donald',
    'Washington',
    date(1946, 6, 14),
    None,
    date(2017, 1, 20),
    None,
    'Queens',
    'New York',
    'Republican',
)

print(p2, '\n')
